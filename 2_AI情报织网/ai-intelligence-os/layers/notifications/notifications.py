"""
Notifications - 推送通知集成
支持 Telegram、企业微信、Email、飞书
"""
import os
import smtplib
import json
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional

from core.logger import get_logger

logger = get_logger("Notifications")


class TelegramNotifier:
    """Telegram机器人推送"""

    def __init__(self, bot_token: str = None, chat_id: str = None):
        self.bot_token = bot_token or os.environ.get('TELEGRAM_BOT_TOKEN')
        self.chat_id = chat_id or os.environ.get('TELEGRAM_CHAT_ID')
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}" if self.bot_token else None

    def send_message(self, text: str, parse_mode: str = 'Markdown') -> bool:
        """发送消息"""
        if not self.api_url:
            logger.warning("Telegram not configured")
            return False

        try:
            import requests
            url = f"{self.api_url}/sendMessage"
            data = {
                'chat_id': self.chat_id,
                'text': text[:4096],
                'parse_mode': parse_mode
            }
            resp = requests.post(url, json=data, timeout=10)
            return resp.status_code == 200
        except Exception as e:
            logger.error(f"Telegram send failed: {e}")
            return False

    def send_daily_brief(self, brief_content: str) -> bool:
        """发送日报摘要"""
        lines = [
            "📡 *AI Intelligence Daily*\n",
            f"生成时间: {self._now_str()}\n",
            "=" * 30,
            brief_content[:3500]
        ]
        return self.send_message('\n'.join(lines))

    def _now_str(self) -> str:
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M')


class WeComNotifier:
    """企业微信推送"""

    def __init__(self, webhook_url: str = None):
        self.webhook_url = webhook_url or os.environ.get('WECOM_WEBHOOK_URL')

    def send_message(self, content: str) -> bool:
        """发送消息"""
        if not self.webhook_url:
            logger.warning("WeCom webhook not configured")
            return False

        try:
            import requests
            data = {
                "msgtype": "text",
                "text": {
                    "content": content[:4096]
                }
            }
            resp = requests.post(self.webhook_url, json=data, timeout=10)
            return resp.status_code == 200
        except Exception as e:
            logger.error(f"WeCom send failed: {e}")
            return False

    def send_markdown(self, content: str) -> bool:
        """发送Markdown消息"""
        if not self.webhook_url:
            return False

        try:
            import requests
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "content": content[:4096]
                }
            }
            resp = requests.post(self.webhook_url, json=data, timeout=10)
            return resp.status_code == 200
        except Exception as e:
            logger.error(f"WeCom markdown send failed: {e}")
            return False


class FeishuNotifier:
    """飞书推送（通过飞书开放平台 API 直接调用）"""

    def __init__(self, account_id: str = "rainbow", user_id: str = None):
        self.account_id = account_id
        self.user_id = user_id or 'ou_7a2313a4cb3f0d60920571a8200075b4'
        # 从 openclaw.json 读取的飞书应用凭证（account: rainbow）
        self.app_id = 'cli_a95523e8dae1dcc4'
        self.app_secret = 'eqBQcLXKn5525PcKFKguIcrkukRo1F3v'
        self._tenant_token = None
        self._token_expires_at = 0

    def _get_tenant_token(self) -> str:
        """获取 tenant_access_token"""
        import time
        import requests
        if self._tenant_token and time.time() < self._token_expires_at - 300:
            return self._tenant_token
        try:
            resp = requests.post(
                'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
                json={'app_id': self.app_id, 'app_secret': self.app_secret},
                timeout=10
            )
            data = resp.json()
            if data.get('code') == 0:
                self._tenant_token = data['tenant_access_token']
                self._token_expires_at = time.time() + data.get('expire', 7200)
                logger.info("Feishu tenant token obtained")
                return self._tenant_token
            else:
                logger.error(f"Feishu token error: {data}")
                return None
        except Exception as e:
            logger.error(f"Feishu token fetch error: {e}")
            return None

    def _strip_markdown(self, text: str) -> str:
        """移除 Markdown 格式符号（飞书 text 不支持 Markdown）"""
        import re
        # 移除 **bold** -> bold
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        # 移除 *italic* -> italic（仅当两边不是中文时）
        text = re.sub(r'(?<![\u4e00-\u9fff\u3400-\u4dbf])\*(.+?)\*(?![\u4e00-\u9fff\u3400-\u4dbf])', r'\1', text)
        return text

    def send_message(self, content: str, user_id: str = None) -> bool:
        """通过飞书开放平台 API 发送消息给用户（支持加粗）"""
        import requests
        import json
        target = user_id or self.user_id
        token = self._get_tenant_token()
        if not token:
            logger.error("Feishu: no tenant token")
            return False


        for raw_line in lines:
            line = raw_line.rstrip()
            stripped = line.strip()

            if not stripped:
                post_elements.append({'tag': 'text', 'text': '\n'})
                continue

            # ── 1. 分类全宽加粗行 **标题**（加粗） ──
            if re.match(r'^\*\*[^*]+\*\*$', stripped):
                inner = re.sub(r'\*\*(.+?)\*\*', r'\1', stripped)
                post_elements.append({'tag': 'text', 'text': inner, 'style': ['bold']})
                post_elements.append({'tag': 'text', 'text': '\n'})
                continue

            # ── 2. 字段行 ** [xxx]**: yyy（仅标签加粗，内容不加粗） ──
            if stripped.startswith('**') and re.search(r'\*\*:', stripped):
                m = re.match(r'^\*\*(.+?)\*\*:(.*)', stripped)
                if m:
                    inner, rest = m.group(1), m.group(2)
                    if inner.startswith('[') and ']' in inner:
                        label = inner[1:inner.index(']')]
                        if label in CORE_LABELS:
                            post_elements.append({'tag': 'text', 'text': label, 'style': ['bold']})
                            post_elements.append({'tag': 'text', 'text': rest + '\n'})
                        else:
                            # 子项标签不加粗
                            post_elements.append({'tag': 'text', 'text': label + ': ' + rest.lstrip() + '\n'})
                        continue
                    elif inner.startswith('【') and '】' in inner:
                        label = inner[1:inner.index('】')]
                        if label in CORE_LABELS:
                            post_elements.append({'tag': 'text', 'text': label, 'style': ['bold']})
                            post_elements.append({'tag': 'text', 'text': rest + '\n'})
                        else:
                            post_elements.append({'tag': 'text', 'text': label + ': ' + rest.lstrip() + '\n'})
                        continue
                # fallback
                post_elements.append({'tag': 'text', 'text': stripped[2:]})
                post_elements.append({'tag': 'text', 'text': '\n'})
                continue

            # ── 3. 普通字段行 [xxx]: yyy（无 ** 前缀） ──
            if stripped.startswith('[') and ':' in stripped:
                idx = stripped.index(':')
                label = stripped[1:idx]
                rest = stripped[idx + 1:]
                if label in CORE_LABELS:
                    post_elements.append({'tag': 'text', 'text': label, 'style': ['bold']})
                    post_elements.append({'tag': 'text', 'text': rest + '\n'})
                else:
                    post_elements.append({'tag': 'text', 'text': stripped + '\n'})
                continue

            # ── 4. 子弹项 • xxx 或 - xxx（都不加粗） ──
            if stripped.startswith('•') or stripped.startswith('- '):
                content_text = stripped.lstrip('•-').strip()
                post_elements.append({'tag': 'text', 'text': '  • ' + content_text + '\n'})
                continue

            # ── 5. 其他所有行（不加粗） ──
            post_elements.append({'tag': 'text', 'text': stripped})
            post_elements.append({'tag': 'text', 'text': '\n'})

        for raw_line in lines:
            line = raw_line.rstrip()
            stripped = line.strip()

            if not stripped:
                elements.append({'tag': 'text', 'text': '\n'})
                continue

            # ── 1. 分类全宽加粗行 **标题**（加粗） ──
            if re.match(r'^\*\*[^*]+\*\*$', stripped):
                inner = re.sub(r'\*\*(.+?)\*\*', r'\1', stripped)
                elements.append({'tag': 'text', 'text': inner, 'style': ['bold']})
                elements.append({'tag': 'text', 'text': '\n'})
                continue

            # ── 2. 字段行 ** [xxx]**: yyy（仅标签加粗，内容不加粗） ──
            if stripped.startswith('**') and re.search(r'\*\*:', stripped):
                m = re.match(r'^\*\*(.+?)\*\*:(.*)', stripped)
                if m:
                    inner, rest = m.group(1), m.group(2)
                    if inner.startswith('[') and ']' in inner:
                        label = inner[1:inner.index(']')]
                        if label in CORE_LABELS:
                            elements.append({'tag': 'text', 'text': label, 'style': ['bold']})
                            elements.append({'tag': 'text', 'text': rest + '\n'})
                        else:
                            # 子项标签不加粗
                            elements.append({'tag': 'text', 'text': label + ': ' + rest.lstrip() + '\n'})
                        continue
                    elif inner.startswith('【') and '】' in inner:
                        label = inner[1:inner.index('】')]
                        if label in CORE_LABELS:
                            elements.append({'tag': 'text', 'text': label, 'style': ['bold']})
                            elements.append({'tag': 'text', 'text': rest + '\n'})
                        else:
                            elements.append({'tag': 'text', 'text': label + ': ' + rest.lstrip() + '\n'})
                        continue
                # fallback
                elements.append({'tag': 'text', 'text': stripped[2:]})
                elements.append({'tag': 'text', 'text': '\n'})
                continue

            # ── 3. 普通字段行 [xxx]: yyy（无 ** 前缀） ──
            if stripped.startswith('[') and ':' in stripped:
                idx = stripped.index(':')
                label = stripped[1:idx]
                rest = stripped[idx + 1:]
                if label in CORE_LABELS:
                    elements.append({'tag': 'text', 'text': label, 'style': ['bold']})
                    elements.append({'tag': 'text', 'text': rest + '\n'})
                else:
                    elements.append({'tag': 'text', 'text': stripped + '\n'})
                continue

            # ── 4. 子弹项 • xxx 或 - xxx（都不加粗） ──
            if stripped.startswith('•') or stripped.startswith('- '):
                content_text = stripped.lstrip('•-').strip()
                elements.append({'tag': 'text', 'text': '  • ' + content_text + '\n'})
                continue

            # ── 5. 其他所有行（不加粗） ──
            elements.append({'tag': 'text', 'text': stripped})
            elements.append({'tag': 'text', 'text': '\n'})
        post_content = {
            'zh_cn': {
                'title': 'AI 情报织网 · 每日精选',
                'content': [[element] for element in post_elements]
            }
        }

        try:
            url = 'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id'
            headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
            payload = {
                'receive_id': target,
                'msg_type': 'post',
                'content': json.dumps(post_content, ensure_ascii=False)
            }
            resp = requests.post(url, headers=headers, json=payload, timeout=15)
            result = resp.json()
            if result.get('code') == 0:
                logger.info(f"Feishu post message sent to {target}")
                return True
            else:
                logger.error(f"Feishu post failed: {result}")
                return False
        except Exception as e:
            logger.error(f"Feishu send error: {e}")
            return False

    def send_message_text_only(self, content: str, user_id: str = None) -> bool:
        """纯文本发送（无格式）"""
        import requests
        import json
        target = user_id or self.user_id
        token = self._get_tenant_token()
        if not token:
            logger.error("Feishu: no tenant token")
            return False
        plain_content = self._strip_markdown(content)
        try:
            url = 'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id'
            headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
            payload = {
                'receive_id': target,
                'msg_type': 'text',
                'content': json.dumps({'text': plain_content})
            }
            resp = requests.post(url, headers=headers, json=payload, timeout=15)
            result = resp.json()
            if result.get('code') == 0:
                logger.info(f"Feishu text message sent to {target}")
                return True
            else:
                logger.error(f"Feishu send failed: {result}")
                return False
        except Exception as e:
            logger.error(f"Feishu send error: {e}")
            return False

    def send_daily_brief(self, brief_content: str) -> bool:
        """发送每日报告摘要（支持加粗）"""
        from datetime import datetime
        header = f"📡 *AI 情报织网 · 每日精选*\n📅 {datetime.now().strftime('%Y-%m-%d')}\n\n"
        return self.send_message(header + brief_content)

    def send_message(self, content: str, user_id: str = None) -> bool:
        """通过飞书开放平台 API 发送富文本消息（支持加粗）"""
        import requests
        import json
        import re
        target = user_id or self.user_id
        token = self._get_tenant_token()
        if not token:
            logger.error("Feishu: no tenant token")
            return False

        def feishu_bold(txt):
            import re
            txt = re.sub(r'\*\*(.+?)\*\*', r'*\1*', txt)
            txt = re.sub(r'\*(.+?)\*', r'\1', txt)
            return txt

        lines = content.split('\n')
        elements = []

        for raw_line in lines:
            line = raw_line.rstrip()
            stripped = line.strip()

            if not stripped:
                elements.append({'tag': 'text', 'text': '\n'})
                continue

            # 一级标题行（emoji开头）
            if stripped.startswith(('📡', '🔥', '💡', '📊', '🤖', '⚡')):
                bold_line = feishu_bold(stripped)
                elements.append({'tag': 'text', 'text': bold_line, 'style': ['bold']})
                elements.append({'tag': 'text', 'text': '\n'})

            # 全宽加粗行 **text**
            elif re.match(r'^\*\*[^*]+\*\*$', stripped):
                inner = feishu_bold(stripped[2:-2])
                elements.append({'tag': 'text', 'text': inner, 'style': ['bold']})
                elements.append({'tag': 'text', 'text': '\n'})

            # 字段行 [xxx]：yyy 或 **[xxx]**：yyy（加粗标签）
            elif stripped.startswith('[') and ':' in stripped:
                idx = stripped.index(':')
                raw_label = stripped[:idx]  # 如 [一句话总结] 或 **[一句话总结]**
                rest = stripped[idx + 1:]
                # 提取标签文字（去掉 **）
                label_text = raw_label.strip()
                if label_text.startswith('**'):
                    label_text = label_text[2:-2]
                elements.append({'tag': 'text', 'text': label_text, 'style': ['bold']})
                if rest.strip():
                    elements.append({'tag': 'text', 'text': rest + '\n'})
                else:
                    elements.append({'tag': 'text', 'text': '\n'})

            # 【xxx】：yyy（加粗标签）
            elif stripped.startswith('【') and '】：' in stripped:
                idx = stripped.index(':')
                raw_label = stripped[:idx + 2]
                rest = stripped[idx + 2:]
                label_text = raw_label.strip()
                if label_text.startswith('**'):
                    label_text = label_text[2:-2]
                elements.append({'tag': 'text', 'text': label_text, 'style': ['bold']})
                if rest.strip():
                    elements.append({'tag': 'text', 'text': rest})
                elements.append({'tag': 'text', 'text': '\n'})

            # 子项 • xxx 或 - xxx
            elif stripped.startswith('•') or stripped.startswith('- '):
                bullet_content = stripped.lstrip('•-').strip()
                elements.append({'tag': 'text', 'text': '  • '})
                elements.append({'tag': 'text', 'text': bullet_content, 'style': ['bold']})
                elements.append({'tag': 'text', 'text': '\n'})

            # 字段行 ** [xxx]：yyy（带 ** 前缀，冒号为单字节 ：）
            elif stripped.startswith('**') and ':' in stripped:
                norm = stripped[2:]
                idx = norm.index(':')
                raw_label = norm[:idx]
                rest = norm[idx + 1:]
                label_text = raw_label.strip().lstrip('**').rstrip('**')
                elements.append({'tag': 'text', 'text': label_text, 'style': ['bold']})
                if rest.strip():
                    elements.append({'tag': 'text', 'text': rest + '\n'})
                else:
                    elements.append({'tag': 'text', 'text': '\n'})

            # 【xxx】：yyy（可能带 ** 前缀）
            elif stripped.startswith('**') and '】：' in stripped:
                norm = stripped[2:]
                idx = norm.index(':')
                raw_label = norm[:idx + 2]
                rest = norm[idx + 2:]
                label_text = raw_label.strip().lstrip('**').rstrip('**')
                elements.append({'tag': 'text', 'text': label_text, 'style': ['bold']})
                if rest.strip():
                    elements.append({'tag': 'text', 'text': rest})
                elements.append({'tag': 'text', 'text': '\n'})

            # 普通内容行（先去掉外层 **）
            else:
                norm = stripped
                if norm.startswith('**') and norm.endswith('**') and norm.count('**') == 2:
                    inner = norm[2:-2]
                    elements.append({'tag': 'text', 'text': inner, 'style': ['bold']})
                else:
                    if norm.startswith('**'):
                        norm = norm[2:]
                    bold_line = feishu_bold(norm)
                    elements.append({'tag': 'text', 'text': bold_line})
                elements.append({'tag': 'text', 'text': '\n'})

        post_content = {
            'zh_cn': {
                'title': 'AI 情报织网 · 每日精选',
                'content': [[el] for el in elements]
            }
        }

        try:
            url = 'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id'
            headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
            payload = {
                'receive_id': target,
                'msg_type': 'post',
                'content': json.dumps(post_content, ensure_ascii=False)
            }
            resp = requests.post(url, headers=headers, json=payload, timeout=15)
            result = resp.json()
            if result.get('code') == 0:
                logger.info(f"Feishu post message sent to {target}")
                return True
            else:
                logger.error(f"Feishu post failed: {result}")
                return False
        except Exception as e:
            logger.error(f"Feishu send error: {e}")
            return False


class EmailNotifier:
    """邮件推送"""

    def __init__(self, smtp_server: str = None, smtp_port: int = 587,
                 username: str = None, password: str = None,
                 from_addr: str = None, to_addrs: List[str] = None):
        self.smtp_server = smtp_server or os.environ.get('SMTP_SERVER')
        self.smtp_port = smtp_port or int(os.environ.get('SMTP_PORT', '587'))
        self.username = username or os.environ.get('SMTP_USERNAME')
        self.password = password or os.environ.get('SMTP_PASSWORD')
        self.from_addr = from_addr or os.environ.get('SMTP_FROM')
        self.to_addrs = to_addrs or os.environ.get('SMTP_TO', '').split(',')

    def send_email(self, subject: str, body: str, html: bool = False) -> bool:
        """发送邮件"""
        if not self.smtp_server:
            logger.warning("Email not configured")
            return False

        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.from_addr
            msg['To'] = ', '.join(self.to_addrs)

            if html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.from_addr, self.to_addrs, msg.as_string())

            logger.info(f"Email sent: {subject}")
            return True
        except Exception as e:
            logger.error(f"Email send failed: {e}")
            return False

    def send_daily_brief(self, brief_content: str) -> bool:
        """发送日报"""
        from datetime import datetime
        subject = f"AI Intelligence Daily - {datetime.now().strftime('%Y-%m-%d')}"
        return self.send_email(subject, brief_content)


class NotificationCenter:
    """
    通知中心
    统一管理多种推送渠道
    """

    def __init__(self):
        self.telegram = TelegramNotifier()
        self.wecom = WeComNotifier()
        self.email = EmailNotifier()
        self.feishu = FeishuNotifier()

    def notify_all(self, content: str, channels: List[str] = None) -> Dict:
        """通过多个渠道发送通知"""
        if channels is None:
            channels = ['telegram', 'wecom', 'email', 'feishu']

        results = {}
        for channel in channels:
            if channel == 'telegram':
                results['telegram'] = self.telegram.send_message(content)
            elif channel == 'wecom':
                results['wecom'] = self.wecom.send_markdown(content)
            elif channel == 'email':
                results['email'] = self.email.send_email(
                    f"AI Intelligence Update - {self._now_str()}",
                    content
                )
            elif channel == 'feishu':
                results['feishu'] = self.feishu.send_message(content)

        return results

    def send_daily_report(self, report_content: str, channels: List[str] = None) -> Dict:
        """发送每日报告"""
        if channels is None:
            channels = ['telegram', 'wecom', 'feishu']

        results = {}
        for channel in channels:
            if channel == 'telegram':
                results['telegram'] = self.telegram.send_daily_brief(report_content)
            elif channel == 'wecom':
                header = f"📡 *AI Intelligence Daily*\n📅 {self._now_str()}\n\n"
                results['wecom'] = self.wecom.send_markdown(header + report_content[:3500])
            elif channel == 'email':
                results['email'] = self.email.send_daily_brief(report_content)
            elif channel == 'feishu':
                results['feishu'] = self.feishu.send_daily_brief(report_content)

        return results

    def _now_str(self) -> str:
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M')


def create_notification_center() -> NotificationCenter:
    """创建通知中心"""
    return NotificationCenter()


def send_test_notification(channel: str = 'telegram') -> bool:
    """发送测试通知"""
    nc = create_notification_center()
    test_msg = f"✅ AI Intelligence OS 测试消息\n时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n如果你看到这条消息，说明推送配置正确。"
    from datetime import datetime
    return nc.notify_all(test_msg, channels=[channel])