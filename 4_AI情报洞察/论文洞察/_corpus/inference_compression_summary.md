# 推理压缩论文筛选报告

**筛选日期**: 2026-06-26

**论文库总数**: 27784
**筛选出论文数**: 2808
**筛选阈值**: score >= 2

## 类别分布

- **压缩基础**: 899篇
- **量化基础**: 463篇
- **稀疏化**: 414篇
- **MoE基础**: 325篇
- **长上下文**: 171篇
- **投机解码**: 85篇
- **KV Cache基础**: 65篇
- **推理延迟**: 21篇
- **量化感知训练**: 15篇
- **推理效率**: 10篇
- **量化方法**: 10篇
- **分布式推理**: 10篇
- **推理吞吐**: 9篇
- **MoE通信**: 6篇
- **P/D分离**: 2篇
- **KV管理**: 1篇

## 高相关论文 (Top 50)

1. **MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding**
   - 分数: 15.0 | 类别: 推理延迟, 推理吞吐, 投机解码
   - 链接: https://openreview.net/pdf?id=CS2JWaziYr

2. **CASAK-V: Dynamic Sparse Attention and Adaptive KV-Cache Compression for Memory-Efficient Long-Context LLM Inference**
   - 分数: 13.0 | 类别: KV Cache基础, 压缩基础, 稀疏化
   - 链接: N/A

3. **VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration**
   - 分数: 11.0 | 类别: KV Cache基础, 压缩基础, 稀疏化
   - 链接: https://openreview.net/pdf?id=HMrcv7Q4Ub

4. **ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference**
   - 分数: 11.0 | 类别: KV Cache基础, 推理吞吐, 长上下文
   - 链接: N/A

5. **SALS: Sparse Attention in Latent Space for KV Cache Compression**
   - 分数: 11.0 | 类别: KV Cache基础, 压缩基础, 稀疏化
   - 链接: N/A

6. **PyramidInfer: Pyramid KV Cache Compression for High-throughput LLM Inference**
   - 分数: 11.0 | 类别: KV Cache基础, 压缩基础, 推理吞吐
   - 链接: https://aclanthology.org/2024.findings-acl.195.pdf

7. **ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference**
   - 分数: 10.0 | 类别: KV Cache基础, 压缩基础, 长上下文
   - 链接: N/A

8. **KV-Dict: Sparse KV Cache Compression with Universal Dictionaries**
   - 分数: 10.0 | 类别: KV Cache基础, 压缩基础, 稀疏化
   - 链接: N/A

9. **Efficient Expert Pruning for Sparse Mixture-of-Experts Language Models: Enhancing Performance and Reducing Inference Costs**
   - 分数: 10.0 | 类别: 压缩基础, 稀疏化, MoE基础
   - 链接: N/A

10. **DynamicKV: Task-Aware Adaptive KV Cache Compression for Long Context LLMs**
   - 分数: 10.0 | 类别: KV Cache基础, 压缩基础, 长上下文
   - 链接: N/A

11. **ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference**
   - 分数: 10.0 | 类别: KV Cache基础, 压缩基础, 长上下文
   - 链接: N/A

12. **MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference**
   - 分数: 10.0 | 类别: KV Cache基础, 压缩基础, 稀疏化
   - 链接: N/A

13. **$\text{S}^2$Q-VDiT: Accurate Quantized Video Diffusion Transformer with Salient Data and Sparse Token Distillation**
   - 分数: 10.0 | 类别: 量化基础, 压缩基础, 稀疏化
   - 链接: N/A

14. **A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts**
   - 分数: 10.0 | 类别: 压缩基础, 稀疏化, MoE基础
   - 链接: https://openreview.net/pdf?id=1oU4FKpVx5

15. **KV Cache Compression, But What Must We Give in Return? A Comprehensive Benchmark of Long Context Capable Approaches**
   - 分数: 10.0 | 类别: KV Cache基础, 压缩基础, 长上下文
   - 链接: https://aclanthology.org/2024.findings-emnlp.266.pdf

16. **Unlocking Data-free Low-bit Quantization with Matrix Decomposition for KV Cache Compression**
   - 分数: 10.0 | 类别: KV Cache基础, 量化基础, 压缩基础
   - 链接: https://aclanthology.org/2024.acl-long.133.pdf

17. **Replicate and Quantize: A Plug-and-Play Strategy for Load Balancing in Sparse Mixture-of-Experts LLMs**
   - 分数: 9 | 类别: 量化基础, 稀疏化, MoE基础
   - 链接: N/A

18. **Efficient Bayesian DNN Compression through Sparse Quantized Sub-distributions**
   - 分数: 9 | 类别: 量化基础, 压缩基础, 稀疏化
   - 链接: N/A

19. **SVDQuant: Absorbing Outliers by Low-Rank Component for 4-Bit Diffusion Models**
   - 分数: 9.0 | 类别: 量化基础, 压缩基础
   - 链接: https://openreview.net/pdf?id=vWR3KuiQur

20. **ALTER: All-in-One Layer Pruning and Temporal Expert Routing for Efficient Diffusion Generation**
   - 分数: 9 | 类别: 压缩基础, MoE基础, MoE通信
   - 链接: N/A

21. **Inference-Time Hyper-Scaling with KV Cache Compression**
   - 分数: 9.0 | 类别: KV Cache基础, 压缩基础
   - 链接: N/A

22. **MoESD: Unveil Speculative Decoding's Potential for Accelerating Sparse MoE**
   - 分数: 9 | 类别: 稀疏化, MoE基础, 投机解码
   - 链接: N/A

23. **SNAP-TTA: Sparse Test-Time Adaptation for Latency-Sensitive Applications**
   - 分数: 8.0 | 类别: 稀疏化, 推理延迟
   - 链接: N/A

24. **EfficientQAT: Efficient Quantization-Aware Training for Large Language Models**
   - 分数: 8.0 | 类别: 量化基础, 量化感知训练
   - 链接: N/A

25. **OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition**
   - 分数: 8.0 | 类别: 压缩基础, 稀疏化
   - 链接: https://openreview.net/pdf?id=DLDuVbxORA

26. **LoRC: Low-Rank Compression for LLMs KV Cache with a Progressive Compression Strategy**
   - 分数: 8.0 | 类别: KV Cache基础, 压缩基础
   - 链接: N/A

27. **LogQuant: Log-Distributed 2-Bit Quantization of KV Cache with Superior Accuracy Preservation**
   - 分数: 8.0 | 类别: KV Cache基础, 量化基础
   - 链接: N/A

28. **COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training**
   - 分数: 8.0 | 类别: 量化基础, 压缩基础
   - 链接: https://openreview.net/pdf?id=XfKSDgqIRj

29. **SinkQ: Accurate 2-bit KV Cache Quantization with Dynamic Sink Tracking**
   - 分数: 8.0 | 类别: KV Cache基础, 量化基础
   - 链接: N/A

30. **Mixture Compressor for Mixture-of-Experts LLMs Gains More**
   - 分数: 8.0 | 类别: 压缩基础, MoE基础
   - 链接: https://openreview.net/pdf?id=hheFYjOsWO

31. **MoA: Mixture of Sparse Attention for Automatic Large Language Model Compression**
   - 分数: 8.0 | 类别: 压缩基础, 稀疏化
   - 链接: N/A

32. **Towards Efficient Mixture of Experts: A Holistic Study of Compression Techniques**
   - 分数: 8.0 | 类别: 压缩基础, MoE基础
   - 链接: N/A

33. **Examining Post-Training Quantization for Mixture-of-Experts: A Benchmark**
   - 分数: 8.0 | 类别: 量化基础, MoE基础
   - 链接: N/A

34. **FedQLoRA: Federated Quantization-Aware LoRA for Large Language Models**
   - 分数: 8.0 | 类别: 量化基础, 量化感知训练
   - 链接: N/A

35. **StructMoE: Augmenting MoEs with Hierarchically Routed Low Rank Experts**
   - 分数: 8.0 | 类别: 压缩基础, MoE基础
   - 链接: N/A

36. **QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead**
   - 分数: 8.0 | 类别: KV Cache基础, 量化基础
   - 链接: N/A

37. **Retraining-Free Merging of Sparse Mixture-of-Experts via Hierarchical Clustering**
   - 分数: 8.0 | 类别: 稀疏化, MoE基础
   - 链接: N/A

38. **SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference**
   - 分数: 8.0 | 类别: KV Cache基础, 压缩基础
   - 链接: N/A

39. **Discovering Important Experts for Mixture-of-Experts Models Pruning Through a Theoretical Perspective**
   - 分数: 8.0 | 类别: 压缩基础, MoE基础
   - 链接: N/A

40. **SNAP: Low-Latency Test-Time Adaptation with Sparse Updates**
   - 分数: 8.0 | 类别: 稀疏化, 推理延迟
   - 链接: N/A

41. **CryptoMoE: Privacy-Preserving and Scalable Mixture of Experts Inference via Balanced Expert Routing**
   - 分数: 8.0 | 类别: MoE基础, MoE通信
   - 链接: N/A

42. **KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction**
   - 分数: 8.0 | 类别: KV Cache基础, 压缩基础
   - 链接: N/A

43. **Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression**
   - 分数: 8.0 | 类别: KV Cache基础, 压缩基础
   - 链接: N/A

44. **SeerAttention: Self-distilled Attention Gating for Efficient Long-context Prefilling**
   - 分数: 8.0 | 类别: 压缩基础, 长上下文
   - 链接: N/A

45. **DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs**
   - 分数: 8.0 | 类别: 压缩基础, 稀疏化
   - 链接: N/A

46. **PAROAttention: Pattern-Aware ReOrdering for Efficient Sparse and Quantized Attention in Visual Generation Models**
   - 分数: 8.0 | 类别: 量化基础, 稀疏化
   - 链接: N/A

47. **Domain-Specific Pruning of Large Mixture-of-Experts Models with Few-shot Demonstrations**
   - 分数: 8.0 | 类别: 压缩基础, MoE基础
   - 链接: N/A

48. **Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity**
   - 分数: 8.0 | 类别: 稀疏化, 推理吞吐
   - 链接: N/A

49. **Homogeneous Keys, Heterogeneous Values: Exploiting Local KV Cache Asymmetry for Long-Context LLMs**
   - 分数: 8.0 | 类别: KV Cache基础, 长上下文
   - 链接: N/A

50. **InfiniPot-V: Memory-Constrained KV Cache Compression for Streaming Video Understanding**
   - 分数: 8.0 | 类别: KV Cache基础, 压缩基础
   - 链接: N/A

