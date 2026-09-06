# 推理压缩论文筛选报告 v3

**日期**: 2026-06-26
**论文库总数**: 27784
**推理压缩论文数**: 2155

## 按压缩对象统计

- **通信(Comm)**: 338篇
- **状态(State/KV)**: 109篇
- **参数(Weights)**: 39篇

## 按压缩方法统计

- **量化(Quant)**: 462篇
- **蒸馏(Distill)**: 434篇
- **稀疏(Sparse)**: 418篇
- **低秩(LowRank)**: 349篇
- **剪枝(Prune)**: 186篇

## 对象×方法矩阵

| 对象 | 方法 | 论文数 |
|------|------|--------|
| 其他 | 量化(Quant) | 425 |
| 其他 | 蒸馏(Distill) | 425 |
| 其他 | 稀疏(Sparse) | 387 |
| 其他 | 低秩(LowRank) | 329 |
| 通信(Comm) | 其他 | 289 |
| 其他 | 剪枝(Prune) | 172 |
| 状态(State/KV) | 其他 | 87 |
| 参数(Weights) | 量化(Quant) | 28 |
| 通信(Comm) | 稀疏(Sparse) | 22 |
| 通信(Comm) | 低秩(LowRank) | 10 |
| 通信(Comm) | 剪枝(Prune) | 10 |
| 通信(Comm) | 蒸馏(Distill) | 8 |
| 状态(State/KV) | 稀疏(Sparse) | 7 |
| 状态(State/KV) | 低秩(LowRank) | 7 |
| 状态(State/KV) | 量化(Quant) | 7 |
| 参数(Weights) | 其他 | 6 |
| 通信(Comm) | 量化(Quant) | 3 |
| 参数(Weights) | 低秩(LowRank) | 3 |
| 参数(Weights) | 剪枝(Prune) | 2 |
| 状态(State/KV) | 剪枝(Prune) | 2 |
| 参数(Weights) | 稀疏(Sparse) | 2 |
| 状态(State/KV) | 蒸馏(Distill) | 1 |

## Top 50 论文

1. **Replicate and Quantize: A Plug-and-Play Strategy for Load Balancing in Sparse Mixture-of-Experts LLMs**
   - 分数: 3 | 对象: 通信(Comm) | 方法: 量化(Quant), 稀疏(Sparse)

2. **OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition**
   - 分数: 3 | 对象:  | 方法: 剪枝(Prune), 稀疏(Sparse), 低秩(LowRank)

3. **Efficient Expert Pruning for Sparse Mixture-of-Experts Language Models: Enhancing Performance and Reducing Inference Costs**
   - 分数: 3 | 对象: 通信(Comm) | 方法: 剪枝(Prune), 稀疏(Sparse)

4. **SLiM: One-shot Quantized Sparse Plus Low-rank Approximation of LLMs**
   - 分数: 3 | 对象:  | 方法: 量化(Quant), 稀疏(Sparse), 低秩(LowRank)

5. **SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs**
   - 分数: 3 | 对象:  | 方法: 剪枝(Prune), 稀疏(Sparse), 低秩(LowRank)

6. **Q-GaLore: Quantized GaLore with INT4 Projection and Layer-Adaptive Low-Rank Gradients**
   - 分数: 3 | 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)

7. **MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference**
   - 分数: 3 | 对象: 状态(State/KV) | 方法: 剪枝(Prune), 稀疏(Sparse)

8. **FPSAttention: Training-Aware FP8 and Sparsity Co-Design for Fast Video Diffusion**
   - 分数: 3 | 对象: 参数(Weights) | 方法: 量化(Quant), 稀疏(Sparse)

9. **$\text{S}^2$Q-VDiT: Accurate Quantized Video Diffusion Transformer with Salient Data and Sparse Token Distillation**
   - 分数: 3 | 对象:  | 方法: 量化(Quant), 稀疏(Sparse), 蒸馏(Distill)

10. **A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts**
   - 分数: 3 | 对象: 通信(Comm) | 方法: 剪枝(Prune), 稀疏(Sparse)

11. **MoE-I2: Compressing Mixture of Experts Models through Inter-Expert Pruning and Intra-Expert Low-Rank Decomposition**
   - 分数: 3 | 对象: 通信(Comm) | 方法: 剪枝(Prune), 低秩(LowRank)

12. **IntactKV: Improving Large Language Model Quantization by Keeping Pivot Tokens Intact**
   - 分数: 3 | 对象: 参数(Weights), 状态(State/KV) | 方法: 量化(Quant)

13. **Unlocking Data-free Low-bit Quantization with Matrix Decomposition for KV Cache Compression**
   - 分数: 3 | 对象: 状态(State/KV) | 方法: 量化(Quant), 低秩(LowRank)

14. **LLM Compression with Convex Optimization—Part 1: Weight Quantization**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 量化(Quant)

15. **FedComLoc: Communication-Efficient Distributed Training of Sparse and Quantized Models**
   - 分数: 2 | 对象:  | 方法: 量化(Quant), 稀疏(Sparse)

16. **Does Vector Quantization Fail in Spatio-Temporal Forecasting? Exploring a Differentiable Sparse Soft-Vector Quantization Approach**
   - 分数: 2 | 对象:  | 方法: 量化(Quant), 稀疏(Sparse)

17. **You Only Prune Once: Designing Calibration-Free Model Compression With Policy Learning**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 剪枝(Prune)

18. **Distribution-Aware Diffusion Model Quantization via Distortion Minimization**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 量化(Quant)

19. **Hydra-MDP++: Advancing End-to-End Driving via Hydra-Distillation with Expert-Guided Decision Analysis**
   - 分数: 2 | 对象: 通信(Comm) | 方法: 蒸馏(Distill)

20. **MoDeGPT: Modular Decomposition for Large Language Model Compression**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 低秩(LowRank)

21. **Distilling the Knowledge in Data Pruning**
   - 分数: 2 | 对象:  | 方法: 剪枝(Prune), 蒸馏(Distill)

22. **Sparse Attention Decomposition Applied to Circuit Tracing**
   - 分数: 2 | 对象:  | 方法: 稀疏(Sparse), 低秩(LowRank)

23. **CDQuant: Accurate Post-training Weight Quantization of LLMs using Greedy Coordinate Descent**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 量化(Quant)

24. **SOLOS: Sparse Optimization For Long Sequence In Context Compression Enhanced LLMs**
   - 分数: 2 | 对象: 状态(State/KV) | 方法: 稀疏(Sparse)

25. **Scaling FP8 training to trillion-token LLMs**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 量化(Quant)

26. **Low-Rank Correction for Quantized LLMs**
   - 分数: 2 | 对象:  | 方法: 量化(Quant), 低秩(LowRank)

27. **KV-Dict: Sparse KV Cache Compression with Universal Dictionaries**
   - 分数: 2 | 对象: 状态(State/KV) | 方法: 稀疏(Sparse)

28. **VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration**
   - 分数: 2 | 对象: 状态(State/KV) | 方法: 稀疏(Sparse)

29. **Moirai-MoE: Empowering Time Series Foundation Models with Sparse Mixture of Experts**
   - 分数: 2 | 对象: 通信(Comm) | 方法: 稀疏(Sparse)

30. **LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 量化(Quant)

31. **iQR: Quantile Regression with QR Orthogonal Decomposition for Resource Scheduling Optimization without Empirical Model**
   - 分数: 2 | 对象:  | 方法: 量化(Quant), 低秩(LowRank)

32. **Enhancing single-cell Multi-Modal Multi-Task Learning via Sparse Mixture-of-Experts**
   - 分数: 2 | 对象: 通信(Comm) | 方法: 稀疏(Sparse)

33. **SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 低秩(LowRank)

34. **Multi-expert collaboration: Enhancing heterogeneous knowledge independence and alignment in knowledge distillation**
   - 分数: 2 | 对象: 通信(Comm) | 方法: 蒸馏(Distill)

35. **Palu: KV-Cache Compression with Low-Rank Projection**
   - 分数: 2 | 对象: 状态(State/KV) | 方法: 低秩(LowRank)

36. **MORE: A MIXTURE OF LOW-RANK EXPERTS FOR ADAPTIVE MULTI-TASK LEARNING**
   - 分数: 2 | 对象: 通信(Comm) | 方法: 低秩(LowRank)

37. **Rate/Distortion Constrained Model Quantization for Efficient Storage and Inference**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 量化(Quant)

38. **QP-SNN: Quantized and Pruned Spiking Neural Networks**
   - 分数: 2 | 对象:  | 方法: 量化(Quant), 剪枝(Prune)

39. **LoRC: Low-Rank Compression for LLMs KV Cache with a Progressive Compression Strategy**
   - 分数: 2 | 对象: 状态(State/KV) | 方法: 低秩(LowRank)

40. **LogQuant: Log-Distributed 2-Bit Quantization of KV Cache with Superior Accuracy Preservation**
   - 分数: 2 | 对象: 状态(State/KV) | 方法: 量化(Quant)

41. **Prune at the Clients, Not the Server: Accelerated Sparse Training in Federated Learning**
   - 分数: 2 | 对象:  | 方法: 剪枝(Prune), 稀疏(Sparse)

42. **On the Effectiveness of Discrete Representations in Sparse Mixture of Experts**
   - 分数: 2 | 对象: 通信(Comm) | 方法: 稀疏(Sparse)

43. **Adapprox: Memory Efficient Optimization via Adaptive Randomized Low-Rank Approximation**
   - 分数: 2 | 对象: 状态(State/KV) | 方法: 低秩(LowRank)

44. **Medium-Difficulty Samples Constitute Smoothed Decision Boundary for Knowledge Distillation on Pruned Datasets**
   - 分数: 2 | 对象:  | 方法: 剪枝(Prune), 蒸馏(Distill)

45. **Rethinking Knowledge Distillation: A Mixture-of-Experts Perspective**
   - 分数: 2 | 对象: 通信(Comm) | 方法: 蒸馏(Distill)

46. **Fantastic Experts and How to Find Them: A Multi-Dimensional Study for Experts-Level Sparsification in Mixture-of-Experts**
   - 分数: 2 | 对象: 通信(Comm) | 方法: 稀疏(Sparse)

47. **Preserving Large Activations: The Key to KV Cache Pruning**
   - 分数: 2 | 对象: 状态(State/KV) | 方法: 剪枝(Prune)

48. **Rotated Runtime Smooth: Training-Free Activation Smoother for accurate INT4 inference**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 量化(Quant)

49. **Quantum Algorithm for Sparse Online Learning with Truncated Gradient Descent**
   - 分数: 2 | 对象:  | 方法: 量化(Quant), 稀疏(Sparse)

50. **COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training**
   - 分数: 2 | 对象: 参数(Weights) | 方法: 量化(Quant)

