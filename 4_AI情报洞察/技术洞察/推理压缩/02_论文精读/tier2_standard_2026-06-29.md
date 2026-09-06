# Tier 2 推荐论文（v2 标准精读）

> 数量: 805篇 | 评分范围: 6-11
> 精读格式：每篇问题背景+核心创新+关键数据

---

## 按关键词分组

### quantization（270篇）

- **[9] [ICLR 2025] Effective Interplay between Sparsity and Quantization: From Theor**
  The increasing size of deep neural networks (DNNs) necessitates effective model compression to reduce their computational and memory footprints. Spars

- **[9] [ICML 2025] ResQ: Mixed-Precision Quantization of Large Language Models with **
  Post-training quantization (PTQ) of large language models (LLMs) holds the promise in reducing the prohibitive computational cost at inference time. Q

- **[9] [CVPR 2025] MAR-3D: Progressive Masked Auto-regressor for High-Resolution 3D **
  Recent advances in auto-regressive transformers have revolutionized generative modeling across different domains, from language processing to visual g

- **[9] [ICLR 2025] Surprising Effectiveness of pretraining Ternary Language Model at**
  Rapid advancements in GPU computational power has outpaced memory capacity and bandwidth growth, creating bottlenecks in Large Language Model (LLM) in

- **[9] [CVPR 2025] CASP: Compression of Large Multimodal Models Based on Attention S**
  In this work, we propose an extreme compression technique for Large Multimodal Models (LMMs). While previous studies have explored quantization as an 

- **[9] [CVPR 2025] FIMA-Q: Post-Training Quantization for Vision Transformers by Fis**
  Post-training quantization (PTQ) has stood out as a cost-effective and promising model compression approach over recent years, as it eliminates the ne

- **[9] [CVPR 2025] Towards Improved Text-Aligned Codebook Learning: Multi-Hierarchic**
  Image quantization is a crucial technique in image generation, aimed at learning a codebook that encodes an image into a discrete token sequence. Rece

- **[9] [ICLR 2026] NextStep-1: Toward Autoregressive Image Generation with Continuou**
  Prevailing autoregressive (AR) models for text-to-image generation either rely on heavy, computationally-intensive diffusion models to process continu

- **[9] [ICLR 2026] Latent Speech-Text Transformer**
  Auto-regressive speech-text models are typically pre-trained on a large number of interleaved sequences of text tokens and raw speech encoded as speec

- **[9] [ICLR 2026] LLM Fingerprinting via Semantically Conditioned Watermarks**
  Most LLM fingerprinting methods teach the model to respond to a few fixed queries with predefined atypical responses (keys). This memorization often d

- **[9] [NeurIPS 20] HBLLM: Wavelet-Enhanced High-Fidelity 1-Bit Quantization for LLMs**
  We introduce HBLLM, a wavelet-enhanced high-fidelity $1$-bit post-training quantization method for Large Language Models (LLMs). By leveraging Haar wa

- **[9] [NeurIPS 20] Advanced Sign Language Video Generation with Compressed and Quant**
  Sign Language Video Generation (SLVG) seeks to generate identity-preserving sign language videos from spoken language texts. Existing methods primaril

- **[9] [NeurIPS 20] Win Fast or Lose Slow: Balancing Speed and Accuracy in Latency-Se**
  Large language models (LLMs) have shown remarkable performance across diverse reasoning and generation tasks, and are increasingly deployed as agents 

- **[9] [NeurIPS 20] Vector Quantization in the Brain: Grid-like Codes in World Models**
  We propose Grid-like Code Quantization (GCQ), a brain-inspired method for compressing observation-action sequences into discrete representations using

- **[9] [NeurIPS 20] FPSAttention: Training-Aware FP8 and Sparsity Co-Design for Fast **
  Diffusion generative models have become the standard for producing high-quality, coherent video content, yet their slow inference speeds and high comp

- **[9] [NeurIPS 20] UniTok: a Unified Tokenizer for Visual Generation and Understandi**
  Visual generative and understanding models typically rely on distinct tokenizers to process images, presenting a key challenge for unifying them withi

- **[9] [NeurIPS 20] FP4 All the Way: Fully Quantized Training of Large Language Model**
  We demonstrate, for the first time, fully quantized training (FQT) of large language models (LLMs) using predominantly 4-bit floating-point (FP4) prec

- **[9] [NeurIPS 20] Adaptive Prediction-Powered AutoEval with Reliability and Efficie**
  Selecting  artificial intelligence (AI) models, such as large language models (LLMs), from multiple candidates requires accurate performance estimatio

- **[9] [ICML 2025] From Weight-Based to State-Based Fine-Tuning: Further Memory Redu**
  The LoRA method has achieved notable success in reducing GPU memory usage by applying low-rank updates to weight matrices. Yet, one simple question re

- **[9] [AISTATS 20] Unbiased and Sign Compression in Distributed Learning: Comparing **
  Distributed methods are essential for handling machine learning pipelines comprising large-scale models and datasets. However, their benefits often co


### kv cache（139篇）

- **[9] [ICLR 2025] When Attention Sink Emerges in Language Models: An Empirical View**
  Auto-regressive language Models (LMs) assign significant attention to the first token, even if it is not semantically important, which is known as **a

- **[9] [ICLR 2025] DeFT: Decoding with Flash Tree-attention for Efficient Tree-struc**
  Large language models (LLMs) are increasingly employed for complex tasks that process multiple generation calls in a tree structure with shared prefix

- **[9] [ICLR 2026] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reaso**
  The long-output context generation of large reasoning models enables extended chain of thought (CoT) but also drives rapid growth of the key–value (KV

- **[9] [ICLR 2026] SANA-Video: Efficient Video Generation with Block Linear Diffusio**
  We introduce SANA-Video, a small diffusion model that can efficiently generate videos up to 720×1280 resolution and minute-length duration. SANA-Video

- **[9] [ICLR 2026] MotionStream: Real-Time Video Generation with Interactive Motion **
  Current motion-conditioned video generation methods suffer from prohibitive latency (minutes per video) and non-causal processing that prevents real-t

- **[9] [NeurIPS 20] SmallKV: Small Model Assisted Compensation of KV Cache Compressio**
  KV cache eviction has emerged as an effective solution to alleviate resource constraints faced by LLMs in long-context scenarios. However, existing to

- **[9] [NeurIPS 20] LaViDa: A Large Diffusion Model for Vision-Language Understanding**
  Modern Vision-Language Models (VLMs) can solve a wide range of tasks requiring visual reasoning. In real-world scenarios, desirable properties for VLM

- **[9] [NeurIPS 20] Tensor Product Attention Is All You Need**
  Scaling language models to handle longer input sequences typically necessitates large key-value (KV) caches, resulting in substantial memory overhead 

- **[9] [NeurIPS 20] KVzip: Query-Agnostic KV Cache Compression with Context Reconstru**
  Transformer-based large language models (LLMs) cache context as key-value (KV) pairs during inference. As context length grows, KV cache sizes expand,

- **[9] [NeurIPS 20] TransMLA: Migrating GQA Models to MLA with Full DeepSeek Compatib**
  Modern large-language models often face communication bottlenecks on current hardware rather than computational limitations.  *Multi-head latent atten

- **[9] [NeurIPS 20] Self Forcing: Bridging the Train-Test Gap in Autoregressive Video**
  We introduce Self Forcing, a novel training paradigm for autoregressive video diffusion models. It addresses the longstanding issue of exposure bias, 

- **[9] [NeurIPS 20] QSVD: Efficient Low-rank Approximation for Unified Query-Key-Valu**
  Vision-Language Models (VLMs) are integral to tasks such as image captioning and visual question answering, but their high computational cost, driven 

- **[9] [ICML 2025] RAPID: Long-Context Inference with Retrieval-Augmented Speculativ**
  The emergence of long-context large language models (LLMs) offers a promising alternative to traditional retrieval-augmented generation (RAG) for proc

- **[6] [ICLR 2025] Not All Heads Matter: A Head-Level KV Cache Compression Method wi**
  Key-Value (KV) caching is a common technique to enhance the computational efficiency of Large Language Models (LLMs), but its memory overhead grows ra

- **[6] [ICLR 2025] RobustKV: Defending Large Language Models against Jailbreak Attac**
  Jailbreak attacks circumvent LLMs' built-in safeguards by concealing harmful queries within adversarial prompts. While most existing defenses attempt 

- **[6] [ICLR 2025] A Little Goes a Long Way: Efficient Long Context Training and Inf**
  Training and serving long-context large language models (LLMs) incurs substantial overhead.  To address this, two critical steps are often required: a

- **[6] [ICLR 2025] MatryoshkaKV: Adaptive KV Compression via Trainable Orthogonal Pr**
  KV cache has become a *de facto* technique for the inference of large language models (LLMs), where tensors of shape (layer number, head number, seque

- **[6] [ICML 2025] Lexico: Extreme KV Cache Compression via Sparse Coding over Unive**
  We introduce Lexico, a novel KV cache compression method that leverages sparse coding with a universal dictionary. Our key finding is that key-value c

- **[6] [CVPR 2025] TopV: Compatible Token Pruning with Inference Time Optimization f**
  Vision-Language Models (VLMs) demand substantial computational resources during inference, largely due to the extensive visual input tokens for repres

- **[6] [ICLR 2025] OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs**
  During the inference phase of Large Language Models (LLMs) with long context, a substantial portion of GPU memory is allocated to the KV cache, with m


### speculative decoding（68篇）

- **[9] [ICLR 2025] Faster Cascades via Speculative Decoding**
  Cascades and speculative decoding are two common approaches to improving language models' inference efficiency.  Both approaches interleave two models

- **[9] [ICLR 2025] Judge Decoding: Faster Speculative Sampling Requires Going Beyond**
  The performance of large language models (LLMs) is closely linked to their underlying size, leading to ever-growing networks and hence slower inferenc

- **[9] [ICLR 2026] Overcoming Joint Intractability with Lossless Hierarchical Specul**
  Verification is a key bottleneck in improving inference speed while maintaining distribution fidelity in Speculative Decoding. Recent work has shown t

- **[9] [ICLR 2026] Speculative Actions: A Lossless Framework for Faster AI Agents**
  AI agents have attracted growing interest across industry and academia, but in practice their execution can be slow. For example, letting two state-of

- **[9] [NeurIPS 20] SpecMER: Fast Protein Generation with K-mer Guided Speculative De**
  Autoregressive models have transformed protein engineering by enabling the generation of novel protein sequences beyond those found in nature. However

- **[9] [NeurIPS 20] SpecEdge: Scalable Edge-Assisted Serving Framework for Interactiv**
  Large language models (LLMs) power many modern applications, but serving them at scale remains costly and resource-intensive. Current server-centric s

- **[9] [NeurIPS 20] MoESD: Unveil Speculative Decoding's Potential for Accelerating S**
  Large Language Models (LLMs) have achieved remarkable success across many applications, with Mixture of Experts (MoE) models demonstrating great poten

- **[9] [NeurIPS 20] SuffixDecoding: Extreme Speculative Decoding for Emerging AI Appl**
  Speculative decoding is widely adopted to reduce latency in large language model (LLM) inference by leveraging smaller draft models capable of handlin

- **[9] [NeurIPS 20] Accelerating Diffusion LLMs via Adaptive Parallel Decoding**
  The generation speed of LLMs are bottlenecked by autoregressive decoding, where tokens are predicted sequentially one by one. Alternatively, diffusion

- **[9] [ICML 2025] Accelerating LLM Inference with Lossless Speculative Decoding Alg**
  Accelerating the inference of large language models (LLMs) is a critical challenge in generative AI. Speculative decoding (SD) methods offer substanti

- **[6] [ICLR 2025] Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM**
  Large language models (LLMs) have achieved remarkable success across diverse tasks, yet their inference processes are hindered by substantial time and

- **[6] [ICLR 2025] Block Verification Accelerates Speculative Decoding**
  Speculative decoding is an  effective method for lossless acceleration of large language models during inference. It uses a fast model to draft a bloc

- **[6] [ICLR 2025] Towards Optimal Multi-draft Speculative Decoding**
  Large Language Models (LLMs) have become an indispensable part of natural language processing tasks. However, autoregressive sampling has become an ef

- **[6] [ICLR 2025] Efficient Inference for Large Language Model-based Generative Rec**
  Large Language Model (LLM)-based generative recommendation has achieved notable success, yet its practical deployment is costly particularly due to ex

- **[6] [ICLR 2025] Mixture of Attentions For Speculative Decoding**
  The growth in the number of parameters of Large Language Models (LLMs) has led to a significant surge in computational requirements, making them chall

- **[6] [EMNLP 2024] Draft on the Fly: Adaptive Self-Speculative Decoding using Cosine**
  We present a simple on the fly method for faster inference of large language models. Unlike other (self-)speculative decoding techniques, our method d

- **[6] [ICML 2025] Speculate, then Collaborate: Fusing Knowledge of Language Models **
  Large Language Models (LLMs) often excel in specific domains but fall short in others due to the limitations of their training. Thus, enabling LLMs to

- **[6] [ICLR 2025] PEARL: Parallel Speculative Decoding with Adaptive Draft Length**
  Speculative decoding (SD), where an extra draft model is employed to provide multiple **draft** tokens first and then the original target model verifi

- **[6] [ICML 2025] Gumiho: A Hybrid Architecture to Prioritize Early Tokens in Specu**
  Speculative decoding (SPD) aims to accelerate the auto-regressive token generation process of a target Large Language Model (LLM). Some approaches emp

- **[6] [ICML 2025] polybasic Speculative Decoding Through a Theoretical Perspective**
  Inference latency stands as a critical bottleneck in the large-scale deployment of Large Language Models (LLMs). Speculative decoding methods have rec


### moe （59篇）

- **[9] [ICLR 2025] Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Fr**
  While large language models (LLMs) excel on generation tasks, their decoder-only architecture often limits their potential as embedding models if no f

- **[9] [CVPR 2025] CL-MoE: Enhancing Multimodal Large Language Model with Dual Momen**
  Multimodal large language models (MLLMs) have garnered widespread attention from researchers due to their remarkable understanding and generation capa

- **[9] [ICLR 2025] ChartMoE: Mixture of Diversely Aligned Expert Connector for Chart**
  Automatic chart understanding is crucial for content comprehension and document parsing. Multimodal Large Language Models (MLLMs) have demonstrated re

- **[9] [ICML 2025] Mixture of Lookup Experts**
  Mixture-of-Experts (MoE) activates only a subset of experts during inference, allowing the model to maintain low inference FLOPs and latency even as t

- **[9] [ICLR 2026] Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Re**
  Mixture-of-Experts (MoE) language models dramatically expand model capacity and achieve remarkable performance without increasing per-token compute. H

- **[9] [NeurIPS 20] FlexOLMo: Open Language Models for Flexible Data Use**
  We introduce FlexOLMo, a new class of language models (LMs) that supports (1) distributed training without data sharing, where different model paramet

- **[9] [NeurIPS 20] Advancing Expert Specialization for Better MoE**
  Mixture-of-Experts (MoE) models enable efficient scaling of large language models (LLMs) by activating only a subset of experts per input.  However, w

- **[6] [ICLR 2025] Solving Token Gradient Conflict in Mixture-of-Experts for Large V**
  The Mixture-of-Experts (MoE) has gained increasing attention in studying Large Vision-Language Models (LVLMs). It uses a sparse model to replace the d

- **[6] [ICLR 2025] Ada-K Routing: Boosting the Efficiency of MoE-based LLMs**
  In the era of Large Language Models (LLMs), Mixture-of-Experts (MoE) architectures offer a promising approach to managing computational costs while sc

- **[6] [ICLR 2025] Tight Clusters Make Specialized Experts**
  Sparse Mixture-of-Experts (MoE) architectures have emerged as a promising approach to decoupling model capacity from computational cost. At the core o

- **[6] [ICLR 2025] Layerwise Recurrent Router for Mixture-of-Experts**
  The scaling of large language models (LLMs) has revolutionized their capabilities in various tasks, yet this growth must be matched with efficient com

- **[6] [ICLR 2025] EC-DIT: Scaling Diffusion Transformers with Adaptive Expert-Choic**
  Diffusion transformers have been widely adopted for text-to-image synthesis. While scaling these models up to billions of parameters shows promise, th

- **[6] [ICML 2025] Scaling Laws for Upcycling Mixture-of-Experts Language Models**
  Pretraining large language models (LLMs) is resource-intensive, often requiring months of training time even with high-end GPU clusters.  There are tw

- **[6] [ICML 2025] FloE: On-the-Fly MoE Inference on Memory-constrained GPU**
  With the widespread adoption of Mixture-of-Experts (MoE) models, there is a growing demand for efficient inference on memory-constrained devices. Whil

- **[6] [ICML 2025] R2-T2: Re-Routing in Test-Time for Multimodal Mixture-of-Experts**
  In large multimodal models (LMMs), the perception of non-language modalities (e.g., visual representations) is usually not on par with the large langu

- **[6] [ICLR 2026] Routing Matters in MoE: Scaling Diffusion Transformers with Expli**
  Mixture-of-Experts (MoE) has emerged as a powerful paradigm for scaling model capacity while preserving computational efficiency. Despite its notable 

- **[6] [ICLR 2026] Not All Models Suit Expert Offloading: On Local Routing Consisten**
  Mixture-of-Experts (MoE) enables efficient scaling of large language models (LLMs) with sparsely activated experts during inference. To effectively de

- **[6] [ICLR 2026] Routing Manifold Alignment Improves Generalization of Mixture-of-**
  Sparse Mixture-of-Experts (MoE) have been widely adopted in recent large language models since it can efficiently scale up the model capability withou

- **[6] [ICLR 2026] Towards Greater Leverage: Scaling Laws for Efficient Mixture-of-E**
  Mixture-of-Experts (MoE) has become a dominant architecture for scaling Large Language Models (LLMs) efficiently by decoupling total parameters from c

- **[6] [ICLR 2026] MoBE: Mixture-of-Basis-Experts for Compressing MoE-based LLMs**
  The Mixture-of-Experts (MoE) architecture has become a predominant paradigm for scaling large language models (LLMs). Despite offering strong performa


### pruning（47篇）

- **[9] [NeurIPS 20] Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ P**
  Leveraging attention sparsity to accelerate long-context large language models (LLMs) has been of great importance recently. However, most existing sp

- **[8] [ICLR 2025] Cut the Crap: An Economical Communication Pipeline for LLM-based **
  Recent advancements in large language model (LLM)-powered agents have shown that collective intelligence can significantly outperform individual capab

- **[8] [ICML 2025] SANA 1.5: Efficient Scaling of Training-Time and Inference-Time C**
  This paper presents SANA-1.5, a linear Diffusion Transformer for efficient scaling in text-to-image generation. Building upon SANA-1.0, we introduce t

- **[8] [CVPR 2025] Adversarial Diffusion Compression for Real-World Image Super-Reso**
  Real-world image super-resolution (Real-ISR) aims to reconstruct high-resolution images from low-resolution inputs degraded by complex, unknown proces

- **[8] [CVPR 2025] ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Model**
  Large Vision Language Models (LVLMs) have achieved significant success across multi-modal tasks. However, the computational cost of processing long vi

- **[8] [ICML 2025] Autoformulation of Mathematical Optimization Models Using LLMs**
  Mathematical optimization is fundamental to decision-making across diverse domains, from operations research to healthcare. Yet, translating real-worl

- **[8] [EMNLP 2024] Change Is the Only Constant: Dynamic LLM Slicing based on Layer R**
  This paper introduces a novel model compression approach through dynamic layer-specific pruning in Large Language Models (LLMs), enhancing the traditi

- **[8] [EMNLP 2024] Pruning Foundation Models for High Accuracy without Retraining**
  Despite the superior performance, it is challenging to deploy large language models (LLMs) due to their massive parameters and computations. While pru

- **[8] [CVPR 2025] A Stitch in Time Saves Nine: Small VLM is a Precise Guidance for **
  Vision-language models (VLMs) have shown remarkable success across various multi-modal tasks, yet large VLMs encounter significant efficiency challeng

- **[6] [CVPR 2025] TinyFusion: Diffusion Transformers Learned Shallow**
  Diffusion Transformers have demonstrated remarkable capabilities in image generation but often come with excessive parameterization, resulting in cons

- **[6] [ICLR 2025] Streamlining Redundant Layers to Compress Large Language Models**
  This paper introduces LLM-Streamline, a pioneer work on layer pruning for large language models (LLMs). It is based on the observation that different 

- **[6] [EMNLP 2024] MoE-I2: Compressing Mixture of Experts Models through Inter-Exper**
  The emergence of Mixture of Experts (MoE) LLMs has significantly advanced the development of language models. Compared to traditional LLMs, MoE LLMs o

- **[6] [CVPR 2025] FirePlace: Geometric Refinements of LLM Common Sense Reasoning fo**
  Scene generation with 3D assets presents a complex challenge, requiring both high-level semantic understanding and low-level geometric reasoning. Whil

- **[6] [ICLR 2025] How new data permeates LLM knowledge and how to dilute it**
  Large language models continually learn through the accumulation of gradient-based updates, but how individual pieces of new information affect existi

- **[6] [ICLR 2025] Improving the Sparse Structure Learning of Spiking Neural Network**
  The human brain utilizes spikes for information transmission and dynamically reorganizes its network structure to boost energy efficiency and cognitiv

- **[6] [ICML 2025] Occult: Optimizing Collaborative Communications across Experts fo**
  Mixture-of-experts (MoE) architectures could achieve impressive computational efficiency with expert parallelism, which relies heavily on all-to-all c

- **[6] [ICML 2025] Delta Decompression for MoE-based LLMs Compression**
  Mixture-of-Experts (MoE) architectures in large language models (LLMs) achieve exceptional performance, but face prohibitive storage and memory requir

- **[6] [CVPR 2025] ICP: Immediate Compensation Pruning for Mid-to-high Sparsity**
  The increasing adoption of large-scale models under 7 billion parameters in both language and vision domains enables inference tasks on a single consu

- **[6] [CVPR 2025] Improving Gaussian Splatting with Localized Points Management**
  Point management is critical for optimizing 3D Gaussian Splatting models, as point initiation (e.g., via structure from motion) is often distributiona

- **[6] [CVPR 2025] SURGEON: Memory-Adaptive Fully Test-Time Adaptation via Dynamic A**
  Despite the growing integration of deep models into mobile terminals, the accuracy of these models declines significantly due to various deployment in


### sparse attention（45篇）

- **[9] [ICLR 2025] FlexPrefill: A Context-Aware Sparse Attention Mechanism for Effic**
  Large language models (LLMs) encounter computational challenges during long-sequence inference, especially in the attention pre-filling phase, where t

- **[9] [CVPR 2025] SCSA: A Plug-and-Play Semantic Continuous-Sparse Attention for Ar**
  Attention-based arbitrary style transfer methods, including CNN-based, Transformer-based, and Diffusion-based, have flourished and produced high-quali

- **[9] [NeurIPS 20] MoBA: Mixture of Block Attention for Long-Context LLMs**
  Scaling the effective context length is essential for advancing large language models (LLMs) toward artificial general intelligence (AGI). However, th

- **[9] [NeurIPS 20] Sparse VideoGen2: Accelerate Video Generation with Sparse Attenti**
  Diffusion Transformers (DiTs) are essential for video generation but suffer from significant latency due to the quadratic complexity of attention.  By

- **[9] [NeurIPS 20] CSBrain: A Cross-scale Spatiotemporal Brain Foundation Model for **
  Understanding and decoding human brain activity from electroencephalography (EEG) signals is a fundamental problem in neuroscience and artificial inte

- **[9] [NeurIPS 20] The emergence of sparse attention: impact of data distribution an**
  Emergence is a fascinating property of large language models and neural networks more broadly: as models scale and train for longer, they sometimes de

- **[6] [ICLR 2025] TidalDecode: Fast and Accurate LLM Decoding with Position Persist**
  Large language models (LLMs) have driven significant advancements across diverse NLP tasks, with long-context models gaining prominence for handling e

- **[6] [ICLR 2025] PT-T2I/V: An Efficient Proxy-Tokenized Diffusion Transformer for **
  The global self-attention mechanism in diffusion transformers involves redundant computation due to the sparse and redundant nature of visual informat

- **[6] [ICML 2025] SCENT: Robust Spatiotemporal Learning for Continuous Scientific D**
  Spatiotemporal learning is challenging due to the intricate interplay between spatial and temporal dependencies, the high dimensionality of the data, 

- **[6] [CVPR 2025] Associative Transformer**
  Emerging from the pairwise attention in conventional Transformers, there is a growing interest in sparse attention mechanisms that align more closely 

- **[6] [CVPR 2025] Boltzmann Attention Sampling for Image Analysis with Small Object**
  Detecting and segmenting small objects, such as lung nodules and tumor lesions, remains a critical challenge in image analysis. These objects often oc

- **[6] [CVPR 2025] De^2Gaze: Deformable and Decoupled Representation Learning for 3D**
  3D Gaze estimation is a challenging task due to two main issues. First, existing methods focus on analyzing dense features (e.g., large pixel regions)

- **[6] [CVPR 2025] GoLF-NRT: Integrating Global Context and Local Geometry for Few-S**
  Neural Radiance Fields (NeRF) have transformed novel view synthesis by modeling scene-specific volumetric representations directly from images. While 

- **[6] [CVPR 2025] HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generat**
  Visual AutoRegressive modeling (VAR) shows promise in bridging the speed and quality gap between autoregressive image models and diffusion models. VAR

- **[6] [ICLR 2026] MoGA: Mixture-of-Groups Attention for End-to-End Long Video Gener**
  Long video generation with Diffusion Transformers (DiTs) is bottlenecked by the quadratic scaling of full attention with sequence length. Since attent

- **[6] [ICLR 2026] DSA: Efficient Inference For Video Generation Models via Distribu**
  Diffusion Transformer models have driven the rapid advances in video generation, achieving state-of-the-art quality and flexibility. However, their at

- **[6] [ICLR 2026] Towards Understanding the Nature of Attention with Low-Rank Spars**
  We propose Low-Rank Sparse Attention (Lorsa), a sparse replacement model of Transformer attention layers to disentangle original Multi Head Self Atten

- **[6] [ICLR 2026] Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Ge**
  Auto-regressive (AR) models, initially successful in language generation, have recently shown promise in visual generation tasks due to their superior

- **[6] [ICLR 2026] Long-Context Generalization with Sparse Attention**
  Transformer-based architectures traditionally employ softmax to compute attention weights, which produces dense distributions over all tokens in a seq

- **[6] [ICLR 2026] Long-Context Attention Benchmark: From Kernel Efficiency to Distr**
  Transformer-based large language models (LLMs) have achieved remarkable success, yet their standard attention mechanism incurs quadratic computation a


### distillation（37篇）

- **[9] [NeurIPS 20] AdaSPEC: Selective Knowledge Distillation for Efficient Speculati**
  Speculative Decoding (SD) accelerates large language model inference by employing a small draft model to generate predictions, which are then verified

- **[8] [EMNLP 2024] Learning to Plan for Retrieval-Augmented Large Language Models fr**
  Improving the performance of large language models (LLMs) in complex question-answering (QA) scenarios has always been a research focal point. Recent 

- **[8] [EMNLP 2024] PromptKD: Distilling Student-Friendly Knowledge for Generative La**
  Recent advancements in large language models (LLMs) have raised concerns about inference costs, increasing the need for research into model compressio

- **[8] [CVPR 2025] Diffusion Self-Distillation for Zero-Shot Customized Image Genera**
  Text-to-image diffusion models produce impressive results but are frustrating tools for artists who desire fine-grained control. For example, a common

- **[8] [ICLR 2025] Towards Fast, Specialized Machine Learning Force Fields: Distilli**
  The foundation model (FM) paradigm is transforming Machine Learning Force Fields (MLFFs), leveraging general-purpose representations and scalable trai

- **[8] [ICLR 2025] SuperCorrect: Advancing Small LLM Reasoning with Thought Template**
  Large language models (LLMs) like GPT-4, DeepSeek-R1, and ReasonFlux have shown significant improvements in various reasoning tasks. However, smaller 

- **[8] [CVPR 2025] OSV: One Step is Enough for High-Quality Image to Video Generatio**
  Video diffusion models have shown great potential in generating high-quality videos, making them an increasingly popular focus. However, their inheren

- **[8] [CVPR 2025] Pixel-level and Semantic-level Adjustable Super-resolution: A Dua**
  Diffusion prior-based methods have shown impressive results in real-world image super-resolution (SR). However, most existing methods entangle pixel-l

- **[8] [CVPR 2025] TSD-SR: One-Step Diffusion with Target Score Distillation for Rea**
  Pre-trained text-to-image diffusion models are increasingly applied to real-world image super-resolution (Real-ISR) task. Given the iterative refineme

- **[8] [CVPR 2025] Active Data Curation Effectively Distills Large-Scale Multimodal **
  Knowledge distillation (KD) is the de facto standard for compressing large-scale models into smaller ones. Prior works have explored ever more complex

- **[8] [CVPR 2025] From Slow Bidirectional to Fast Autoregressive Video Diffusion Mo**
  Current video diffusion models achieve impressive generation quality but struggle in interactive applications due to bidirectional attention dependenc

- **[6] [ICLR 2025] Presto! Distilling Steps and Layers for Accelerating Music Genera**
  Despite advances in diffusion-based text-to-music (TTM) methods, efficient, high-quality generation remains a challenge. We introduce Presto!, an appr

- **[6] [CVPR 2025] EMOE: Modality-Specific Enhanced Dynamic Emotion Experts**
  Multimodal Emotion Recognition (MER) aims to predict human emotions by leveraging multiple modalities, such as vision, acoustics, and language. Howeve

- **[6] [ICLR 2025] Open-Vocabulary Customization from CLIP via Data-Free Knowledge D**
  Vision-language models such as CLIP have demonstrated strong zero-shot performance, but their considerable size and inefficient inference limit custom

- **[6] [ICLR 2025] Progressive distillation induces an implicit curriculum**
  Knowledge distillation leverages a teacher model to improve the training of a student model. A persistent challenge is that a better teacher does not 

- **[6] [ICLR 2025] TAID: Temporally Adaptive Interpolated Distillation for Efficient**
  Causal language models have demonstrated remarkable capabilities, but their size poses significant challenges for deployment in resource-constrained e

- **[6] [ICLR 2025] Advantage-Guided Distillation for Preference Alignment in Small L**
  Alignment techniques enable Large Language Models (LLMs) to generate outputs that align with human preferences and play a crucial role in their effect

- **[6] [ICML 2025] DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLM**
  Despite the success of distillation in large language models (LLMs), most prior work applies identical loss functions to both teacher- and student-gen

- **[6] [EMNLP 2024] Temperature-Centric Investigation of Speculative Decoding with Kn**
  Speculative decoding stands as a pivotal technique to expedite inference in autoregressive (large) language models. This method employs a smaller *dra

- **[6] [CVPR 2025] OPTICAL: Leveraging Optimal Transport for Contribution Allocation**
  The demands for increasingly large-scale datasets pose substantial storage and computation challenges to building deep learning models. Dataset distil


### mixture of experts（32篇）

- **[9] [NeurIPS 20] UMoE: Unifying Attention and FFN with Shared Experts**
  Sparse Mixture of Experts (MoE) architectures have emerged as a promising approach for scaling Transformer models. While initial works primarily incor

- **[6] [ICLR 2025] Efficiently Democratizing Medical LLMs for 50 Languages via a Mix**
  Adapting medical Large  Language Models to local languages can reduce barriers to accessing healthcare services, but data scarcity remains a significa

- **[6] [ICLR 2025] Drop-Upcycling: Training Sparse Mixture of Experts with Partial R**
  The Mixture of Experts (MoE) architecture reduces the training and inference cost significantly compared to a dense model of equivalent capacity. Upcy

- **[6] [ICLR 2025] HMoRA: Making LLMs More Effective with Hierarchical Mixture of Lo**
  Recent studies have combined Mixture of Experts (MoE) and Parameter-Efficient Fine-tuning (PEFT) to fine-tune large language models (LLMs), holding ex

- **[6] [ICLR 2025] Ultra-Sparse Memory Network**
  It is widely acknowledged that the performance of Transformer models is logarithmically related to their number of parameters and computational comple

- **[6] [ICLR 2025] More Experts Than Galaxies: Conditionally-Overlapping Experts wit**
  The evolution of biological neural systems has led to both modularity and sparse coding, which enables energy efficiency and robustness across the div

- **[6] [ICLR 2025] TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice**
  The Mixture of Experts (MoE) architecture has emerged as a promising solution to reduce computational overhead by selectively activating subsets of mo

- **[6] [ICLR 2025] Filtered not Mixed: Filtering-Based Online Gating for Mixture of **
  We propose MoE-F — a formalized mechanism for combining N pre-trained expert Large Language Models (LLMs) in online time-series prediction tasks by ad

- **[6] [ICML 2025] Expert Race: A Flexible Routing Strategy for Scaling Diffusion Tr**
  Diffusion models have emerged as mainstream framework in visual generation. Building upon this success, the integration of Mixture of Experts (MoE) me

- **[6] [ICML 2025] Optimizing Robustness and Accuracy in Mixture of Experts: A Dual-**
  Mixture of Experts (MoE) have shown remarkable success in leveraging specialized expert networks for complex machine learning tasks. However, their su

- **[6] [EMNLP 2024] Efficient and Interpretable Grammatical Error Correction with Mix**
  Error type information has been widely used to improve the performance of grammatical error correction (GEC) models, whether for generating correction

- **[6] [CVPR 2025] Correlative and Discriminative Label Grouping for Multi-Label Vis**
  Modeling label correlations has always played a pivotal role in multi-label image classification (MLC), attracting significant attention from research

- **[6] [CVPR 2025] Efficient Data Driven Mixture-of-Expert Extraction from Trained N**
  Vision Transformers (ViTs) have emerged as the state-of-the-art models in various Computer Vision (CV) tasks, but their high computational and resourc

- **[6] [CVPR 2025] Learning Heterogeneous Tissues with Mixture of Experts for Gigapi**
  Analyzing gigapixel Whole Slide Images (WSIs) is challenging due to the complex pathological tissue environment and the absence of target-driven domai

- **[6] [CVPR 2025] Resilient Sensor Fusion Under Adverse Sensor Failures via Multi-M**
  Modern autonomous driving perception systems utilize complementary multi-modal sensors, such as LiDAR and cameras. Although sensor fusion architecture

- **[6] [CVPR 2025] SPMTrack: Spatio-Temporal Parameter-Efficient Fine-Tuning with Mi**
  Most state-of-the-art trackers adopt one-stream paradigm, using a single Vision Transformer for joint feature extraction and relation modeling of temp

- **[6] [ICLR 2026] LinearSR: Unlocking Linear Attention for Stable and Efficient Ima**
  Generative models for Image Super-Resolution (SR) are increasingly powerful, yet their reliance on self-attention's quadratic complexity ($O(N^2)$) cr

- **[6] [ICLR 2026] One-Prompt Strikes Back: Sparse Mixture of Experts for Prompt-bas**
  Prompt-based methods have recently gained prominence in Continual Learning (CL) due to their strong performance and memory efficiency. A prevalent str

- **[6] [ICLR 2026] Revisit Visual Prompt Tuning: The Expressiveness of Prompt Expert**
  Visual Prompt Tuning (VPT) has proven effective for parameter-efficient adaptation of pre-trained vision models to downstream tasks by inserting task-

- **[6] [ICLR 2026] Expert Merging in Sparse Mixture of Experts with Nash Bargaining**
  Existing expert merging strategies for Sparse Mixture of Experts (SMoE) typically rely on input-dependent or input-independent averaging of expert par


### low-rank（28篇）

- **[8] [ICLR 2025] LoLCATs: On Low-Rank Linearizing of Large Language Models**
  Recent works show we can linearize large language models (LLMs)—swapping the quadratic attentions of popular Transformer-based LLMs with subquadratic 

- **[8] [EMNLP 2024] LaMDA: Large Model Fine-Tuning via Spectrally Decomposed Low-Dime**
  Low-rank adaptation (LoRA) has become the default approach to fine-tune large language models (LLMs) due to its significant reduction in trainable par

- **[8] [ICLR 2025] Pareto Low-Rank Adapters: Efficient Multi-Task Learning with Pref**
  Multi-task trade-offs in machine learning can be addressed via Pareto Front Learning (PFL) methods that parameterize the Pareto Front (PF) with a sing

- **[6] [ICML 2025] HealthGPT: A Medical Large Vision-Language Model for Unifying Com**
  We present **HealthGPT**, a powerful Medical Large Vision-Language Model (Med-LVLM) that integrates medical visual comprehension and generation capabi

- **[6] [EMNLP 2024] MiLoRA: Efficient Mixture of Low-Rank Adaptation for Large Langua**
  Low-rank adaptation (LoRA) and its mixture-of-experts (MOE) variants are highly effective parameter-efficient fine-tuning (PEFT) methods. However, the

- **[6] [ICLR 2025] HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large**
  We propose Hadamard High-Rank Adaptation (HiRA), a parameter-efficient fine-tuning (PEFT) method that enhances the adaptability of Large Language Mode

- **[6] [ICLR 2025] SD-LoRA: Scalable Decoupled Low-Rank Adaptation for Class Increme**
  Continual Learning (CL) with foundation models has recently emerged as a promising paradigm to exploit abundant knowledge acquired during pre-training

- **[6] [ICLR 2025] Bilinear MLPs enable weight-based mechanistic interpretability**
  A mechanistic understanding of how MLPs do computation in deep neural net- works remains elusive. Current interpretability work can extract features f

- **[6] [ICML 2025] MoE-SVD: Structured Mixture-of-Experts LLMs Compression via Singu**
  Mixture of Experts (MoE) architecture improves Large Language Models (LLMs) with better scaling, but its higher parameter counts and memory demands cr

- **[6] [ICLR 2025] Nonlinear Sequence Embedding by Monotone Variational Inequality**
  In the wild, we often encounter collections of sequential data such as electrocardiograms, motion capture, genomes, and natural language, and sequence

- **[6] [ICLR 2025] LoRA Done RITE: Robust Invariant Transformation Equilibration for**
  Low-rank adaption (LoRA) is a widely used parameter-efficient finetuning method for LLM that reduces memory requirements. However, current LoRA optimi

- **[6] [ICLR 2025] When is Task Vector Provably Effective for Model Editing? A Gener**
  Task arithmetic refers to editing the pre-trained model by adding a weighted sum of task vectors, each of which is the weight update from the pre-trai

- **[6] [ICML 2025] Autonomy-of-Experts Models**
  Mixture-of-Experts (MoE) models mostly use a router to assign tokens to specific expert modules, activating only partial parameters and often outperfo

- **[6] [ICML 2025] Make LoRA Great Again: Boosting LoRA with Adaptive Singular Value**
  While Low-Rank Adaptation (LoRA) enables parameter-efficient fine-tuning for Large Language Models (LLMs), its performance often falls short of Full F

- **[6] [CVPR 2025] Improving Personalized Search with Regularized Low-Rank Parameter**
  Personalized vision-language retrieval seeks to recognize new concepts (e.g. "my dog Fido") from only a few examples. This task is challenging because

- **[6] [ICLR 2026] Why Low-Precision Transformer Training Fails: An Analysis on Flas**
  The pursuit of computational efficiency has driven the adoption of low-precision formats for training transformer models. However, this progress is of

- **[6] [ICLR 2026] Taming Momentum: Rethinking Optimizer States Through Low-Rank App**
  Modern optimizers like Adam and Muon are central to training large language models, but their reliance on first- and second-order momenta introduces s

- **[6] [ICLR 2026] TD-MoE: Tensor Decomposition for MoE Models**
  Mixture-of-Experts (MoE) architectures have demonstrated remarkable capabilities and scalability for large language models, but incur a prohibitive me

- **[6] [ICLR 2026] LoRA-Mixer: Coordinate Modular LoRA Experts Through Serial Attent**
  Recent attempts to combine low-rank adaptation (LoRA) with mixture-of-experts (MoE) for multi-task adaptation of Large Language Models (LLMs) often re

- **[6] [ICLR 2026] UNITE: Universal kNowledge Integration from Task-specific Experts**
  Large language models (LLMs) with Mixture-of-Experts (MoE) architectures achieve strong performance under sparse activation. However, their expertise 


### sparsity（23篇）

- **[9] [ICLR 2025] Wasserstein Distances, Neuronal Entanglement, and Sparsity**
  Disentangling polysemantic neurons is at the core of many current approaches to interpretability of large language models. Here we attempt to study ho

- **[9] [NeurIPS 20] Mozart: Modularized and Efficient MoE Training on 3.5D Wafer-Scal**
  Mixture-of-Experts (MoE) architecture offers enhanced efficiency for Large Language Models (LLMs) with modularized computation, yet its inherent spars

- **[6] [ICLR 2025] On the Identification of Temporal Causal Representation with Inst**
  Temporally causal representation learning aims to identify the latent causal process from time series observations, but most methods require the assum

- **[6] [ICLR 2025] From Sparse Dependence to Sparse Attention: Unveiling How Chain-o**
  Chain-of-thought (CoT)  significantly enhances the reasoning performance of large language models (LLM). While current theoretical studies often attri

- **[6] [ICLR 2025] SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acc**
  Speculative decoding (SD) has emerged as a widely used paradigm to accelerate LLM inference without compromising quality. It works by first employing 

- **[6] [ICLR 2025] Routing Experts: Learning to Route Dynamic Experts in Existing Mu**
  Recently, mixture of experts (MoE) has become a popular paradigm for achieving the trade-off between modal capacity and efficiency of multimodal large

- **[6] [ICML 2025] Mixture of Experts Made Intrinsically Interpretable**
  Neurons in large language models often exhibit \emph{polysemanticity}, simultaneously encoding multiple unrelated concepts and obscuring interpretabil

- **[6] [ICLR 2026] BLADE: Block-Sparse Attention Meets Step Distillation for Efficie**
  Diffusion transformers currently lead the field in high-quality video generation, but their slow iterative denoising process and prohibitive quadratic

- **[6] [ICLR 2026] DirMoE: Dirichlet-Routed Mixture of Experts**
  Mixture-of-Experts (MoE) models have demonstrated exceptional performance in large-scale language models. Existing routers typically rely on non-diffe

- **[6] [ICLR 2026] Sparse Attention Adaptation for Long Reasoning**
  We introduce SeerAttention-R, a sparse attention framework specifically tailored for the long decoding of reasoning models. Extended from SeerAttentio

- **[6] [ICLR 2026] Sparsity Forcing: Reinforcing Token Sparsity of MLLMs**
  Sparse attention mechanisms aim to reduce computational overhead with minimal accuracy loss by selectively processing salient tokens. Despite their ef

- **[6] [ICLR 2026] Understanding and Improving Length Generalization in Hierarchical**
  Effectively processing long contexts is a critical challenge for language models. While standard Transformers are limited by quadratic complexity and 

- **[6] [ICLR 2026] ProxyAttn: Guided Sparse Attention via Representative Heads**
  The quadratic complexity of attention mechanisms limits the efficiency of Large Language Models (LLMs) on long-text tasks. Recently, methods that dyna

- **[6] [ICLR 2026] vAttention: Verified Sparse Attention via Sampling**
  State-of-the-art sparse attention methods for reducing decoding latency fall into two main categories: approximate top-$k$ (and its extension, top-$p$

- **[6] [NeurIPS 20] Re-ttention: Ultra Sparse Visual Generation via Attention Statist**
  Diffusion Transformers (DiT) have become the de-facto model for generating high-quality visual content like videos and images. A huge bottleneck is th

- **[6] [NeurIPS 20] Delta Attention: Fast and Accurate Sparse Attention Inference by **
  The attention mechanism of a transformer has a quadratic complexity, leading to high inference costs and latency for long sequences. However, attentio

- **[6] [NeurIPS 20] SeerAttention: Self-distilled Attention Gating for Efficient Long**
  Attention is the cornerstone of modern Large Language Models (LLMs). Yet its quadratic complexity hinders efficiency and scalability, especially for l

- **[6] [NeurIPS 20] VORTA: Efficient Video Diffusion via Routing Sparse Attention**
  Video diffusion transformers have achieved remarkable progress in high-quality video generation, but remain computationally expensive due to the quadr

- **[6] [NeurIPS 20] MoE-CAP: Benchmarking Cost, Accuracy and Performance of Sparse Mi**
  The sparse Mixture-of-Experts (MoE) architecture is increasingly favored for scaling Large Language Models (LLMs) efficiently, but it depends on heter

- **[6] [NeurIPS 20] Spark Transformer: Reactivating Sparsity in Transformer FFN and A**
  The discovery of the *lazy neuron phenomenon* (Li et al., 2022), where fewer than 10% of the feedforward networks (FFN) parameters in trained Transfor


### kv-cache（23篇）

- **[9] [NeurIPS 20] Scaling up Test-Time Compute with Latent Reasoning: A Recurrent D**
  We study a novel language model architecture that is capable of scaling test-time computation by implicitly reasoning in latent space.  Our model work

- **[6] [ICLR 2025] Streaming Video Question-Answering with In-context Video KV-Cache**
  We propose ReKV, a novel training-free approach that enables efficient streaming video question-answering (StreamingVQA), by seamlessly integrating wi

- **[6] [ICLR 2025] Scaling up Masked Diffusion Models on Text**
  Masked diffusion models (MDMs) have shown promise in language modeling, yet their scalability and effectiveness in core language tasks, such as text g

- **[6] [ICML 2025] Deliberation in Latent Space via Differentiable Cache Augmentatio**
  Techniques enabling large language models (LLMs) to "think more" by generating and attending to intermediate reasoning steps have shown promise in sol

- **[6] [CVPR 2025] RandAR: Decoder-only Autoregressive Visual Generation in Random O**
  We introduce RandAR, a decoder-only visual autoregressive (AR) model capable of generatng images in arbitrary token orders. Unlike previous decoder-on

- **[6] [ICLR 2025] Palu: KV-Cache Compression with Low-Rank Projection**
  Post-training KV-Cache compression methods typically either sample a subset of effectual tokens or quantize the data into lower numerical bit width. H

- **[6] [ICLR 2026] CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabli**
  Converting pretrained attention modules such as *grouped-query attention* (GQA) into *multi-head latent attention* (MLA) can improve expressivity with

- **[6] [ICLR 2026] ZeroTuning: Unlocking the Initial Token's Power to Enhance Large **
  Token-level attention tuning -- a class of training-free methods including Post-hoc Attention Steering (PASTA) and Attention Calibration (ACT) -- has 

- **[6] [ICLR 2026] Cache-to-Cache: Direct Semantic Communication Between Large Langu**
  Multi-LLM systems harness the complementary strengths of diverse Large Language Models, achieving performance and efficiency gains unattainable by a s

- **[6] [ICLR 2026] Scaling Attention via Feature Sparsity**
  Scaling Transformers to ultra-long contexts is bottlenecked by the $O(n^2 d)$ cost of self-attention. Existing methods reduce this cost along the sequ

- **[6] [ICLR 2026] Task-Related Token Compression in Multimodal Large Language Model**
  Existing Multimodal Large Language Models (MLLMs) process a large number of visual tokens, leading to significant computational costs and inefficiency

- **[6] [ICLR 2026] Learning to Parallel: Accelerating Diffusion Large Language Model**
  Autoregressive decoding in large language models (LLMs) requires $\mathcal{O}(n)$ sequential steps for $n$ tokens, fundamentally limiting inference th

- **[6] [ICLR 2026] KaVa: Latent Reasoning via Compressed KV-Cache Distillation**
  Large Language Models (LLMs) excel at multi-step reasoning problems with explicit chain-of-thought (CoT), but verbose traces incur significant computa

- **[6] [ICLR 2026] Equilibrium Language Models**
  Large Language Models (LLMs) excel across diverse applications but remain impractical for edge deployment due to severe memory bottlenecks at the edge

- **[6] [ICLR 2026] Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis **
  Feedforward models for novel view synthesis (NVS) have recently advanced by transformer-based methods like LVSM, using attention among all input and t

- **[6] [ICLR 2026] IceCache: Memory-Efficient KV-cache Management for Long-Sequence **
  Key-Value (KV) cache plays a pivotal role in accelerating inference in large language models (LLMs) by storing intermediate attention outputs, thereby

- **[6] [NeurIPS 20] dKV-Cache: The Cache for Diffusion Language Models**
  Diffusion Language Models (DLMs) have been seen as a promising competitor for autoregressive language models (ARs). However, diffusion language models

- **[6] [NeurIPS 20] Graph-KV: Breaking Sequence via Injecting Structural Biases into **
  Modern large language models (LLMs) are inherently auto-regressive, requiring input to be serialized into flat sequences regardless of their structura

- **[6] [NeurIPS 20] HELM: Hyperbolic Large Language Models via Mixture-of-Curvature E**
  Frontier large language models (LLMs) have shown great success in text modeling and generation tasks across domains. However, natural language exhibit

- **[6] [NeurIPS 20] Speculate Deep and Accurate: Lossless and Training-Free Accelerat**
  The immense model sizes of large language models (LLMs) challenge deployment on memory-limited consumer GPUs.     Although model compression and param


### prune（9篇）

- **[8] [ICLR 2025] Perturbation-Restrained Sequential Model Editing**
  Model editing is an emerging field that focuses on updating the knowledge embedded within large language models (LLMs) without extensive retraining. H

- **[8] [ICLR 2025] SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretrainin**
  We propose SLoPe, a Double-Pruned **S**parse Plus **L**azy L**o**w-rank Adapter **P**r**e**training method for LLMs that improves the accuracy of spar

- **[6] [ICML 2025] Monte Carlo Tree Diffusion for System 2 Planning**
  Diffusion models have recently emerged as a powerful tool for planning. However, unlike Monte Carlo Tree Search (MCTS)—whose performance naturally imp

- **[6] [ICML 2025] Independence Tests for Language Models**
  Motivated by liability and intellectual property concerns over open-weight models we consider the following problem: given the weights of two models, 

- **[6] [NeurIPS 20] Bigram Subnetworks: Mapping to Next Tokens in Transformer Languag**
  In Transformer language models, activation vectors transform from current token embeddings to next token predictions as they pass through the model. T

- **[6] [NeurIPS 20] ErrorTrace: A Black-Box Traceability Mechanism Based on Model Fam**
  The open-source release of large language models (LLMs) enables malicious users to create unauthorized derivative models at low cost, posing significa

- **[6] [NeurIPS 20] CryptoMoE: Privacy-Preserving and Scalable Mixture of Experts Inf**
  Private large language model (LLM) inference based on cryptographic primitives offers a promising path towards privacy-preserving deep learning. Howev

- **[6] [NeurIPS 20] RobustMerge: Parameter-Efficient Model Merging for MLLMs with Dir**
  Fine-tuning pre-trained models with custom data leads to numerous expert models on specific tasks. Merging models into one universal model to empower 

- **[6] [NeurIPS 20] RepoMaster: Autonomous Exploration and Understanding of GitHub Re**
  The ultimate goal of code agents is to solve complex tasks autonomously.  Although large language models (LLMs) have made substantial progress in code


### key-value cache（8篇）

- **[9] [NeurIPS 20] Hogwild! Inference: Parallel LLM Generation via Concurrent Attent**
  Large Language Models (LLMs) have demonstrated the ability to tackle increasingly complex tasks through advanced reasoning, long-form content generati

- **[9] [NeurIPS 20] Efficient Prompt Compression with Evaluator Heads for Long-Contex**
  Although applications involving long-context inputs are crucial for the effective utilization of large language models (LLMs), they also result in inc

- **[6] [ICML 2025] Cache Me If You Must: Adaptive Key-Value Quantization for Large L**
  Efficient real-world deployments of large language models (LLMs) rely on Key-Value (KV) caching for processing and generating long outputs, reducing t

- **[6] [ICLR 2026] LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-**
  The proliferation of long-context large language models (LLMs) exposes a key bottleneck: the rapidly expanding key-value cache during decoding, which 

- **[6] [NeurIPS 20] LiveStar: Live Streaming Assistant for Real-World Online Video Un**
  Despite significant progress in Video Large Language Models (Video-LLMs) for offline video understanding, existing online Video-LLMs typically struggl

- **[6] [NeurIPS 20] EasySpec: Layer-Parallel Speculative Decoding for Efficient Multi**
  Speculative decoding is an effective and lossless method for Large Language Model (LLM) inference acceleration. It employs a smaller model to generate

- **[6] [ICML 2025] AdaDecode: Accelerating LLM Decoding with Adaptive Layer Parallel**
  Large language models (LLMs) are increasingly used for long-content generation (e.g., long Chain-of-Thought reasoning) where decoding efficiency becom

- **[6] [ACL 2025] Cramming 1568 Tokens into a Single Vector and Back Again: Explori**
  A range of recent works addresses the problem of compression of sequence of tokens into a shorter sequence of real-valued vectors to be used as inputs


### long context（6篇）

- **[9] [ICML 2025] Learning to (Learn at Test Time): RNNs with Expressive Hidden Sta**
  Self-attention performs well in long context but has quadratic complexity. Existing RNN layers have linear complexity, but their performance in long c

- **[6] [ICLR 2025] World Model on Million-Length Video And Language With Blockwise R**
  Enabling long-context understanding remains a key challenge in scaling existing sequence models -- a crucial component in developing generally intelli

- **[6] [EMNLP 2024] LongAlign: A Recipe for Long Context Alignment of Large Language **
  Extending large language models to effectively handle long contexts requires instruction fine-tuning on input sequences of similar length. To address 

- **[6] [ICLR 2025] LongWriter: Unleashing 10,000+ Word Generation from Long Context **
  Current long context large language models (LLMs) can process inputs up to 100,000 tokens, yet struggle to generate outputs exceeding even a modest le

- **[6] [EMNLP 2024] GraphReader: Building Graph-based Agent to Enhance Long-Context A**
  Long-context capabilities are essential for large language models (LLMs) to tackle complex and long-input tasks. Despite numerous efforts made to opti

- **[6] [ICLR 2025] Spider 2.0: Evaluating Language Models on Real-World Enterprise T**
  Real-world enterprise text-to-SQL workflows often involve complex cloud or local data across various database systems, multiple SQL queries in various


### linear attention（2篇）

- **[9] [ICLR 2025] SANA: Efficient High-Resolution Text-to-Image Synthesis with Line**
  We introduce Sana, a text-to-image framework that can efficiently generate images up to 4096$\times$4096 resolution. Sana can synthesize high-resoluti

- **[6] [ICLR 2025] Understanding Factual Recall in Transformers via Associative Memo**
  Large language models have demonstrated an impressive ability to perform factual recall. Prior work has found that transformers trained on factual rec


### prefix caching（2篇）

- **[9] [NeurIPS 20] ElasticMM: Efficient Multimodal LLMs Serving with Elastic Multimo**
  Multimodal large language models (MLLMs) extend LLMs to handle images, videos, and audio by incorporating feature extractors and projection modules. H

- **[6] [ICLR 2026] DPad: Efficient Diffusion Language Models with Suffix Dropout**
  Diffusion-based Large Language Models (dLLMs) parallelize text generation by framing decoding as a denoising process, but suffer from high computation


### quantize（2篇）

- **[6] [ICLR 2025] WavTokenizer: an Efficient Acoustic Discrete Codec Tokenizer for **
  Language models have been effectively applied to modeling natural signals, such as images, video, speech, and audio. A crucial component of these mode

- **[6] [ICML 2025] SpargeAttention: Accurate and Training-free Sparse Attention Acce**
  An efficient attention implementation is essential for large models due to its quadratic time complexity. Fortunately, attention commonly exhibits spa


### tensor parallelism（1篇）

- **[6] [ICLR 2025] LongVILA: Scaling Long-Context Visual Language Models for Long Vi**
  Long-context capability is critical for multi-modal foundation models, especially for long video understanding. We introduce LongVILA, a full-stack so


### sliding window attention（1篇）

- **[6] [ICLR 2025] Samba: Simple Hybrid State Space Models for Efficient Unlimited C**
  Efficiently modeling sequences with infinite context length has long been a challenging problem. Previous approaches have either suffered from quadrat


### cache eviction（1篇）

- **[6] [NeurIPS 20] Learned Prefix Caching for Efficient LLM Inference**
  Prefix caching is a key technique for reducing Large Language Model (LLM) inference costs. However, the prevalent least-recently-used (LRU) eviction a


### matrix decomposition（1篇）

- **[6] [NeurIPS 20] PT-MoE: An Efficient Finetuning Framework for Integrating Mixture**
  Parameter-efficient fine-tuning (PEFT) methods have shown promise in adapting large language models, yet existing approaches exhibit counter-intuitive


### cache compression（1篇）

- **[6] [NeurIPS 20] Value-Guided KV Compression for LLMs via Approximated CUR Decompo**
  Key-value (KV) cache compression has emerged as a critical technique for reducing the memory and latency overhead of autoregressive language models du


