# 推理压缩论文分类报告 v5

**日期**: 2026-06-26
**论文库**: 27784 | **筛选**: 641

## 对象×方法矩阵

| 对象 | 方法 | 论文数 |
|------|------|--------|
| 参数(Weights) | 量化(Quant) | 166 |
| 状态(State/KV) | 稀疏(Sparse) | 128 |
| 参数(Weights) | 蒸馏(Distill) | 121 |
| 参数(Weights) | 低秩(LowRank) | 93 |
| 参数(Weights) | 剪枝(Prune) | 71 |
| 参数(Weights) | 稀疏(Sparse) | 18 |
| 状态(State/KV) | 低秩(LowRank) | 12 |
| 状态(State/KV) | 剪枝(Prune) | 8 |
| 状态(State/KV) | 量化(Quant) | 6 |
| 通信(Comm) | 稀疏(Sparse) | 5 |
| 通信(Comm) | 剪枝(Prune) | 5 |
| 通信(Comm) | 低秩(LowRank) | 3 |
| 状态(State/KV) | 蒸馏(Distill) | 2 |
| 通信(Comm) | 量化(Quant) | 1 |

## Top 50 论文

1. **SLiM: One-shot Quantized Sparse Plus Low-rank Approximation of LLMs**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 量化(Quant), 稀疏(Sparse), 低秩(LowRank)
2. **SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 剪枝(Prune), 稀疏(Sparse), 低秩(LowRank)
3. **$\text{S}^2$Q-VDiT: Accurate Quantized Video Diffusion Transformer with Salient Data and Sparse Token Distillation**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 量化(Quant), 稀疏(Sparse), 蒸馏(Distill)
4. **Dynamic Low-Rank Sparse Adaptation for Large Language Models**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 稀疏(Sparse), 低秩(LowRank)
5. **SP-LoRA: Sparsity-Preserved Low-Rank Adaptation for Sparse Large Language Model**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 稀疏(Sparse), 低秩(LowRank)
6. **SaRA: High-Efficient Diffusion Model Fine-tuning with Progressive Sparse Low-Rank Adaptation**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 稀疏(Sparse), 低秩(LowRank)
7. **SparsitySolver: Efficient Reinforcement Learning-based Pruning for LLMs**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 剪枝(Prune), 稀疏(Sparse)
8. **DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 剪枝(Prune), 稀疏(Sparse)
9. **PAROAttention: Pattern-Aware ReOrdering for Efficient Sparse and Quantized Attention in Visual Generation Models**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 量化(Quant), 稀疏(Sparse)
10. **3BASiL: An Algorithmic Framework for Sparse plus Low-Rank Compression of LLMs**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 稀疏(Sparse), 低秩(LowRank)
11. **Týr-the-Pruner: Structural Pruning LLMs via Global Sparsity Distribution Optimization**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 剪枝(Prune), 稀疏(Sparse)
12. **SqueezeLLM: Dense-and-Sparse Quantization**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 量化(Quant), 稀疏(Sparse)
13. **Outlier Weighed Layerwise Sparsity (OWL): A Missing Secret Sauce for Pruning LLMs to High Sparsity**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 剪枝(Prune), 稀疏(Sparse)
14. **Compressing Large Language Models by Joint Sparsification and Quantization**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 量化(Quant), 稀疏(Sparse)
15. **Low-Rank Approximation for Sparse Attention in Multi-Modal LLMs**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 稀疏(Sparse), 低秩(LowRank)
16. **RoseLoRA: Row and Column-wise Sparse Low-rank Adaptation of Pre-trained Language Model for Knowledge Editing and Fine-tuning**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 稀疏(Sparse), 低秩(LowRank)
17. **NeuroPrune: A Neuro-inspired Topological Sparse Training Algorithm for Large Language Models**
   - 对象: 参数(Weights), 状态(State/KV) | 方法: 剪枝(Prune), 稀疏(Sparse)
18. **Replicate and Quantize: A Plug-and-Play Strategy for Load Balancing in Sparse Mixture-of-Experts LLMs**
   - 对象: 通信(Comm) | 方法: 量化(Quant), 稀疏(Sparse)
19. **OwLore: Outlier-weighed Layerwise Sampled Low-Rank Projection for Memory-Efficient LLM Fine-tuning**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 低秩(LowRank)
20. **Low-Rank Correction for Quantized LLMs**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)
21. **Efficient Expert Pruning for Sparse Mixture-of-Experts Language Models: Enhancing Performance and Reducing Inference Costs**
   - 对象: 通信(Comm) | 方法: 剪枝(Prune), 稀疏(Sparse)
22. **Low Rank Quantization Adaptation for Large Language Model**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)
23. **Low-Rank Quantization-Aware Training for LLMs**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)
24. **IntLoRA: Integral Low-rank Adaptation of Quantized Diffusion Models**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)
25. **From General to Expert: Custom Pruning LLMs Across Language, Domain, and Task**
   - 对象: 通信(Comm), 参数(Weights) | 方法: 剪枝(Prune)
26. **LLM Pruning and Distillation in Practice**
   - 对象: 参数(Weights) | 方法: 剪枝(Prune), 蒸馏(Distill)
27. **SVDQuant: Absorbing Outliers by Low-Rank Component for 4-Bit Diffusion Models**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)
28. **Redefining Experts: Interpretable Decomposition of Language Models for Toxicity Mitigation**
   - 对象: 通信(Comm), 参数(Weights) | 方法: 低秩(LowRank)
29. **MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference**
   - 对象: 状态(State/KV) | 方法: 剪枝(Prune), 稀疏(Sparse)
30. **Value-Guided KV Compression for LLMs via Approximated CUR Decomposition**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 低秩(LowRank)
31. **LQER: Low-Rank Quantization Error Reconstruction for LLMs**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)
32. **GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 低秩(LowRank)
33. **Omni-SMoLA: Boosting Generalist Multimodal Models with Soft Mixture of Low-rank Experts**
   - 对象: 通信(Comm), 参数(Weights) | 方法: 低秩(LowRank)
34. **DL-QAT: Weight-Decomposed Low-Rank Quantization-Aware Training for Large Language Models**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)
35. **Let the Expert Stick to His Last: Expert-Specialized Fine-Tuning for Sparse Architectural Large Language Models**
   - 对象: 通信(Comm), 状态(State/KV) | 方法: 稀疏(Sparse)
36. **QDyLoRA: Quantized Dynamic Low-Rank Adaptation for Efficient Large Language Model Tuning**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 低秩(LowRank)
37. **BitDistiller: Unleashing the Potential of Sub-4-Bit LLMs via Self-Distillation**
   - 对象: 参数(Weights) | 方法: 量化(Quant), 蒸馏(Distill)
38. **Pruning Large Language Models to Intra-module Low-rank Architecture with Transitional Activations**
   - 对象: 参数(Weights) | 方法: 剪枝(Prune), 低秩(LowRank)
39. **Quantized Side Tuning: Fast and Memory-Efficient Tuning of Quantized Large Language Models**
   - 对象: 状态(State/KV), 参数(Weights) | 方法: 量化(Quant)
40. **Faster Language Models with Better Multi-Token Prediction Using Tensor Decomposition**
   - 对象: 参数(Weights) | 方法: 低秩(LowRank)
41. **LLM Compression with Convex Optimization—Part 1: Weight Quantization**
   - 对象: 参数(Weights) | 方法: 量化(Quant)
42. **Multi-aspect Knowledge Distillation with Large Language Model**
   - 对象: 参数(Weights) | 方法: 蒸馏(Distill)
43. **BOND: Aligning LLMs with Best-of-N Distillation**
   - 对象: 参数(Weights) | 方法: 蒸馏(Distill)
44. **LLM Distillation for Efficient Few-Shot Multiple Choice Question Answering**
   - 对象: 参数(Weights) | 方法: 蒸馏(Distill)
45. **LoRA-Composer: Leveraging Low-Rank Adaptation for Multi-Concept Customization in Training-Free Diffusion Models**
   - 对象: 参数(Weights) | 方法: 低秩(LowRank)
46. **SparseVLM: Visual Token Sparsification for Efficient Vision Language Models Inference**
   - 对象: 状态(State/KV) | 方法: 稀疏(Sparse)
47. **Backdoor Attacks for LLMs with Weak-To-Strong Knowledge Distillation**
   - 对象: 参数(Weights) | 方法: 蒸馏(Distill)
48. **Mutual Information Preserving Neural Network Pruning**
   - 对象: 参数(Weights) | 方法: 剪枝(Prune)
49. **Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models**
   - 对象: 状态(State/KV) | 方法: 稀疏(Sparse)
50. **MQuant: Unleashing the Inference Potential of Multimodal Large Language Models via Full Static Quantization**
   - 对象: 参数(Weights) | 方法: 量化(Quant)
