# 推理压缩论文筛选报告 v2

**日期**: 2026-06-26
**论文库总数**: 27784
**筛选出论文数**: 57
**筛选条件**: 压缩对象+方法双重匹配，score >= 4

## 按压缩对象统计

- **通信_MoE**: 16篇
- **参数_权重INT**: 15篇
- **状态_KVCache**: 13篇
- **参数_权重**: 11篇
- **状态_注意力状态**: 2篇

## 按压缩方法统计

- **方法_量化**: 31篇
- **方法_稀疏**: 18篇
- **方法_剪枝**: 5篇
- **方法_低秩**: 3篇
- **方法_蒸馏**: 3篇

## 按对象×方法组合统计

- **参数_权重INT × 方法_量化**: 12篇
- **参数_权重 × 方法_量化**: 11篇
- **通信_MoE × 方法_稀疏**: 10篇
- **状态_KVCache × 方法_量化**: 6篇
- **状态_KVCache × 方法_稀疏**: 5篇
- **通信_MoE × 方法_剪枝**: 3篇
- **通信_MoE × 方法_低秩**: 2篇
- **参数_权重INT × 方法_低秩/方法_量化**: 1篇
- **状态_KVCache × 方法_剪枝/方法_稀疏**: 1篇
- **参数_权重INT × 方法_稀疏/方法_量化**: 1篇
- **状态_KVCache × 方法_剪枝**: 1篇
- **状态_注意力状态 × 方法_稀疏**: 1篇
- **状态_注意力状态 × 方法_蒸馏**: 1篇
- **通信_MoE × 方法_蒸馏**: 1篇
- **参数_权重INT × 方法_蒸馏**: 1篇

## Top 50 论文

1. **SVDQuant: Absorbing Outliers by Low-Rank Component for 4-Bit Diffusion Models**
   - 分数: 7 | 对象: 参数_权重INT | 方法: 方法_量化, 方法_低秩
   - 链接: https://openreview.net/pdf?id=vWR3KuiQur

2. **MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference**
   - 分数: 7 | 对象: 状态_KVCache | 方法: 方法_剪枝, 方法_稀疏
   - 链接: N/A

3. **FPSAttention: Training-Aware FP8 and Sparsity Co-Design for Fast Video Diffusion**
   - 分数: 7 | 对象: 参数_权重INT | 方法: 方法_量化, 方法_稀疏
   - 链接: N/A

4. **Preserving Large Activations: The Key to KV Cache Pruning**
   - 分数: 4.5 | 对象: 状态_KVCache | 方法: 方法_剪枝
   - 链接: N/A

5. **MoESD: Unveil Speculative Decoding's Potential for Accelerating Sparse MoE**
   - 分数: 4.5 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: N/A

6. **LLM Compression with Convex Optimization—Part 1: Weight Quantization**
   - 分数: 4 | 对象: 参数_权重 | 方法: 方法_量化
   - 链接: N/A

7. **Distribution-Aware Diffusion Model Quantization via Distortion Minimization**
   - 分数: 4 | 对象: 参数_权重 | 方法: 方法_量化
   - 链接: N/A

8. **CDQuant: Accurate Post-training Weight Quantization of LLMs using Greedy Coordinate Descent**
   - 分数: 4 | 对象: 参数_权重 | 方法: 方法_量化
   - 链接: N/A

9. **SOLOS: Sparse Optimization For Long Sequence In Context Compression Enhanced LLMs**
   - 分数: 4 | 对象: 状态_注意力状态 | 方法: 方法_稀疏
   - 链接: N/A

10. **Scaling FP8 training to trillion-token LLMs**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: https://openreview.net/pdf?id=E1EHO0imOb

11. **KV-Dict: Sparse KV Cache Compression with Universal Dictionaries**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_稀疏
   - 链接: N/A

12. **VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_稀疏
   - 链接: https://openreview.net/pdf?id=HMrcv7Q4Ub

13. **Moirai-MoE: Empowering Time Series Foundation Models with Sparse Mixture of Experts**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: N/A

14. **LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid**
   - 分数: 4 | 对象: 参数_权重 | 方法: 方法_量化
   - 链接: https://openreview.net/pdf?id=ISqx8giekS

15. **Rate/Distortion Constrained Model Quantization for Efficient Storage and Inference**
   - 分数: 4 | 对象: 参数_权重 | 方法: 方法_量化
   - 链接: N/A

16. **LogQuant: Log-Distributed 2-Bit Quantization of KV Cache with Superior Accuracy Preservation**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_量化
   - 链接: N/A

17. **On the Effectiveness of Discrete Representations in Sparse Mixture of Experts**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: N/A

18. **BCQ: Block Clustered Quantization for 4-bit (W4A4) LLM inference**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: N/A

19. **Rotated Runtime Smooth: Training-Free Activation Smoother for accurate INT4 inference**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: https://openreview.net/pdf?id=WG7GzGx3G9

20. **COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: https://openreview.net/pdf?id=XfKSDgqIRj

21. **BLIMEY: Towards Better Routing Methods in Sparse Mixture of Experts**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: N/A

22. **SinkQ: Accurate 2-bit KV Cache Quantization with Dynamic Sink Tracking**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_量化
   - 链接: N/A

23. **ZipVL: Efficient Large Vision-Language Models with Dynamic Token Sparsification and KV Cache Compression**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_稀疏
   - 链接: N/A

24. **Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: https://openreview.net/pdf?id=gx1wHnf5Vp

25. **Smoothness Bridges Sparsity and Stability in MoEs**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: N/A

26. **MoE-Pruner: Pruning Mixture-of-Experts Large Language Model using the Hints from Its Router**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_剪枝
   - 链接: N/A

27. **Sparse MoE as a New Retriever: Addressing Missing Modality Problem in Incomplete Multimodal Data**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: N/A

28. **QRazor: Reliable and Effortless 4-bit LLM Quantization by Significant Data Razoring**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: N/A

29. **CASAK-V: Dynamic Sparse Attention and Adaptive KV-Cache Compression for Memory-Efficient Long-Context LLM Inference**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_稀疏
   - 链接: N/A

30. **De-biasing Diffusion: Data-Free FP8 Quantization of Text-to-Image Models with Billions of Parameters**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: N/A

31. **KV-Distill: Nearly Lossless Context Compression for Transformers**
   - 分数: 4 | 对象: 状态_注意力状态 | 方法: 方法_蒸馏
   - 链接: N/A

32. **To FP8 and Back Again: Quantifying Reduced Precision Effects on LLM Training Stability**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: N/A

33. **OSTQuant: Refining Large Language Model Quantization with Orthogonal and Scaling Transformations for Better Distribution Fitting**
   - 分数: 4 | 对象: 参数_权重 | 方法: 方法_量化
   - 链接: https://openreview.net/pdf?id=rAcgDBdKnP

34. **Q-GaLore: Quantized GaLore with INT4 Projection and Layer-Adaptive Low-Rank Gradients**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: N/A

35. **LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_蒸馏
   - 链接: https://openreview.net/pdf?id=uWtLOy35WD

36. **StructMoE: Augmenting MoEs with Hierarchically Routed Low Rank Experts**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_低秩
   - 链接: N/A

37. **QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_量化
   - 链接: N/A

38. **ALTER: All-in-One Layer Pruning and Temporal Expert Routing for Efficient Diffusion Generation**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_剪枝
   - 链接: N/A

39. **Towards Fully FP8 GEMM LLM Training at Scale**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: N/A

40. **NSNQuant: A Double Normalization Approach for Calibration-Free Low-Bit Vector Quantization of KV Cache**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_量化
   - 链接: N/A

41. **MoORE: SVD-based Model MoE-ization for Conflict- and Oblivion-Resistant Multi-Task Adaptation**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_低秩
   - 链接: N/A

42. **MoE-CAP: Benchmarking Cost, Accuracy and Performance of Sparse Mixture-of-Experts Systems**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: N/A

43. **FP4 All the Way: Fully Quantized Training of Large Language Models**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: N/A

44. **VETA-DiT: Variance-Equalized and Temporally Adaptive Quantization for Efficient 4-bit Diffusion Transformers**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: N/A

45. **SALS: Sparse Attention in Latent Space for KV Cache Compression**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_稀疏
   - 链接: N/A

46. **KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache**
   - 分数: 4 | 对象: 状态_KVCache | 方法: 方法_量化
   - 链接: https://openreview.net/pdf?id=L057s2Rq8O

47. **$\texttt{MoE-RBench}$: Towards Building Reliable Language Models with Sparse Mixture-of-Experts**
   - 分数: 4 | 对象: 通信_MoE | 方法: 方法_稀疏
   - 链接: https://openreview.net/pdf?id=LyJ85kgHFe

48. **Jetfire: Efficient and Accurate Transformer Pretraining with INT8 Data Flow and Per-Block Quantization**
   - 分数: 4 | 对象: 参数_权重INT | 方法: 方法_量化
   - 链接: https://openreview.net/pdf?id=ltzTHGFF5i

49. **A2Q+: Improving Accumulator-Aware Weight Quantization**
   - 分数: 4 | 对象: 参数_权重 | 方法: 方法_量化
   - 链接: https://openreview.net/pdf?id=mbx2pLK5Eq

50. **Retraining-Free Model Quantization via One-Shot Weight-Coupling Learning**
   - 分数: 4 | 对象: 参数_权重 | 方法: 方法_量化
   - 链接: https://openaccess.thecvf.com/content/CVPR2024/papers/Tang_Retraining-Free_Model_Quantization_via_One-Shot_Weight-Coupling_Learning_CVPR_2024_paper.pdf

