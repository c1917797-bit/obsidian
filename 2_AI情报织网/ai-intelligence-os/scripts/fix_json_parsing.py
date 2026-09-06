import re

with open('layers/paper_analysis/paper_insights.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix: Strip markdown code block wrapper from response before JSON parsing
old_code = '        try:\n            response = self.client.chat([{"role": "user", "content": prompt}], temperature=0.3, max_tokens=800)\n            data = json.loads(response)'

new_code = '''        try:
            response = self.client.chat([{"role": "user", "content": prompt}], temperature=0.3, max_tokens=800)
            # Remove markdown code block wrapper if present
            response = response.strip()
            if response.startswith('```json'):
                response = response[7:]
            elif response.startswith('```'):
                response = response[3:]
            if response.endswith('```'):
                response = response[:-3]
            response = response.strip()
            data = json.loads(response)'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('layers/paper_analysis/paper_insights.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed JSON parsing')
else:
    print('Could not find the code to fix')
    # Try to find similar patterns
    if 'json.loads(response)' in content:
        print('Found json.loads in content')
