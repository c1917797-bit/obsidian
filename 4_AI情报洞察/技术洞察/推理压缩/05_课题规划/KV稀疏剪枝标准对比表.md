| 剪枝标准 | 典型算法 | 优点（实质） | 局限性（实质） |
| :--- | :--- | :--- | :--- |
| 注意力分数统计 | H2O（累计score选Heavy-Hitter）, SnapKV（观测窗口模式投票） | 计算开销极低；SnapKV实现Prefill一次完成、零Decode开销；H2O有(1-1/e)理论保证 | 推理模型CoT中高频自反思Token获高attention但语义冗余，被误保留；H2O多query场景90%预算仍退化；两者均为Query相关，不具通用性 |
| 可恢复动态裁剪 | LazyLLM（被裁Token可按需恢复） | 决策可逆，避免永久删除导致的信息丢失；Prefill+Decode两阶段动态；LLaMA-2-7B多文档QA上2.34倍Prefill加速 | 依赖局部Query每步重评估，计算开销持续；长程记忆差（被裁Token恢复依赖后续Query命中）；仅在单模型单任务验证，泛化性未证 |
| 模型结构先验 | DuoAttention（检索头vs流式头功能区分）, TriAttention（Pre-RoPE三角距离评分） | DuoAttention：头级精确（1.5%KV→97%），NIAH无损，MHA模型2.55倍显存↓+2.18倍Decode加速，3.3M上下文；TriAttention：AIME25 32K=Full Attention，不依赖attention score | DuoAttention：GQA模型压缩受限（头共享KV，仅1.67倍），只保护检索不保护推理链；TriAttention：Pre-RoPE中心假设在非RoPE模型（如ALiBi/NoPE）失效，迁移受限 |
| 语义角色驱动 | KVzip（上下文重构评分，Query无关）, R-KV（冗余感知Score=λ×重要性-(1-λ)×冗余度）, ThinKV（Thought类型R/E/T差异化压缩） | 推理模型场景最优：KVzip 3-4倍压缩Query无关；R-KV 10%KV≈100%性能6.6倍吞吐（SnapKV同预算仅60%）；ThinKV(ICLR'26 Oral) <5%KV 5.8倍吞吐，TPOT 1.68倍低于R-KV | KVzip：上下文重构评分需额外前向传播开销；R-KV：token级冗余检测，大batch下37倍TPOT慢化（ThinKV用CT kernel解决）；ThinKV：Thought分类器需离线训练，Thought类型边界动态界定难 |
