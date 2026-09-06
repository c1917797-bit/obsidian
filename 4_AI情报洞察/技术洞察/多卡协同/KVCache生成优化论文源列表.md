# KVCache生成优化论文源列表

> 基于Obsidian信息源整理，来源包括ICLR 2025、ICML 2024论文数据库

---

## 一、KVCache生成加速（Prefill优化）

### 1. KV-Runahead: Scalable Causal LLM Inference by Parallel Key-Value Cache Generation
| 属性 | 内容 |
|------|------|
| **会议** | ICML 2024 |
| **ID** | OBs0AjXE3F |
| **作者** | Minsik Cho, Mohammad Rastegari, Devang Naik |
| **链接** | https://openreview.net/forum?id=OBs0AjXE3F |
| **PDF** | https://openreview.net/pdf?id=OBs0AjXE3F |
| **Proceedings** | https://proceedings.mlr.press/v235/cho24e.html |

```bibtex
@inproceedings{cho2024kvrunahead,
title={{KV}-Runahead: Scalable Causal {LLM} Inference by Parallel Key-Value Cache Generation},
author={Minsik Cho and Mohammad Rastegari and Devang Naik},
booktitle={Forty-first International Conference on Machine Learning},
year={2024},
url={https://openreview.net/forum?id=OBs0AjXE3F}
}
```

---

### 2. Long Context Compression with Activation Beacon
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | 1eQT9OzfNQ |
| **作者** | Peitian Zhang, Zheng Liu, Shitao Xiao, Ninglu Shao, Qiwei Ye, Zhicheng Dou |
| **链接** | https://openreview.net/forum?id=1eQT9OzfNQ |
| **PDF** | (见OpenReview) |
| **Keywords** | Context Compression; Long Context LLMs; LLM Memory |

```bibtex
@inproceedings{zhang2025long,
title={Long Context Compression with Activation Beacon},
author={Peitian Zhang and Zheng Liu and Shitao Xiao and Ninglu Shao and Qiwei Ye and Zhicheng Dou},
booktitle={The Thirteenth International Conference on Learning Representations},
year={2025},
url={https://openreview.net/forum?id=1eQT9OzfNQ}
}
```

---

### 3. KV Prediction for Improved Time to First Token
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 (Under review) |
| **ID** | QlvL6eEOC6 |
| **作者** | Maxwell Horton, Qingqing Cao, Chenfan Sun, Yanzi Jin, Sachin Mehta, Mohammad Rastegari, Moin Nabi |
| **链接** | https://openreview.net/forum?id=QlvL6eEOC6 |
| **Affiliation** | Apple, Meta Facebook, University of Washington |
| **Keywords** | time to first token; TTFT; on-device; LLM; inference |

```bibtex
@misc{horton2024kv,
title={{KV} Prediction for Improved Time to First Token},
author={Maxwell Horton and Qingqing Cao and Chenfan Sun and Yanzi Jin and Sachin Mehta and Mohammad Rastegari and Moin Nabi},
year={2024},
url={https://openreview.net/forum?id=QlvL6eEOC6}
}
```

---

### 4. LazyLLM: Dynamic Token Pruning for Efficient Long Context LLM Inference
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | 底层论文 |
| **作者** | (待补充) |
| **链接** | https://openreview.net/forum?id=(待检索) |

---

### 5. SwiftKV: Fast Prefill-Optimized Inference with Knowledge-Preserving Model Transformation
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **作者** | (来自vLLM/SGLang生态) |
| **链接** | https://github.com/(待检索) |

---

### 6. UNComp: Uncertainty-Aware Long-context Compressor for Efficient LLM Inference
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **作者** | (待检索) |
| **链接** | https://openreview.net/forum?id=(待检索) |

---

## 二、KVCache存储压缩

### 7. KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache
| 属性 | 内容 |
|------|------|
| **会议** | ICML 2024 |
| **ID** | L057s2Rq8O |
| **作者** | Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen (Henry) Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, Xia Hu |
| **链接** | https://openreview.net/forum?id=L057s2Rq8O |
| **Proceedings** | https://proceedings.mlr.press/v235/liu24bz.html |

```bibtex
@inproceedings{liu2024kivi,
title={{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
author={Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
booktitle={Forty-first International Conference on Machine Learning},
year={2024},
url={https://openreview.net/forum?id=L057s2Rq8O}
}
```

---

### 8. KVSharer: Efficient Inference via Layer-Wise Dissimilar KV Cache Sharing
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | 2Akf4BBCKo |
| **作者** | Yifei Yang, Zouying Cao, Qiguang Chen, Libo Qin, Dongjie Yang, Zhi Chen, Hai Zhao |
| **链接** | https://openreview.net/forum?id=2Akf4BBCKo |
| **Keywords** | Large Language Model; KV Cache; KVSharer |

```bibtex
@misc{yang2024kvsharer,
title={{KVS}harer: Efficient Inference via Layer-Wise Dissimilar {KV} Cache Sharing},
author={Yifei Yang and Zouying Cao and Qiguang Chen and Libo Qin and Dongjie Yang and Zhi Chen and Hai Zhao},
year={2024},
url={https://openreview.net/forum?id=2Akf4BBCKo}
}
```

---

### 9. LSH Tells You What To Discard: An Adaptive Locality-Sensitive Strategy for KV Cache Compression
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | 0ZcQhdyI3n |
| **作者** | Tahseen Rabbani, Minghui Liu, Tony O'Halloran, Ananth Sankaralingam, Mary-Anne Hartley, Furong Huang |
| **链接** | https://openreview.net/forum?id=0ZcQhdyI3n |
| **Affiliation** | Yale University, University of Maryland, National University of Ireland, Galway |
| **Keywords** | kv cache; locality-sensitive hashing; compression |
| **Status** | Withdraw |

```bibtex
@misc{rabbani2025lsh,
title={{LSH} Tells You What To Discard: An Adaptive Locality-Sensitive Strategy for {KV} Cache Compression},
author={Tahseen Rabbani and Minghui Liu and Tony O'Halloran and Ananth Sankaralingam and Mary-Anne Hartley and Furong Huang},
year={2025},
url={https://openreview.net/forum?id=0ZcQhdyI3n}
}
```

---

### 10. MiKV: Mixed-precision KV cache
| 属性 | 内容 |
|------|------|
| **来源** | ICLR 2025 |
| **作者** | (待检索) |

---

### 11. Locret: Enhancing Eviction in Long-Context LLM Inference with Trained Retaining Heads
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | CkCFoN3j4s |
| **作者** | Yuxiang Huang, Binhang Yuan, Xu Han, Chaojun Xiao, Zhiyuan Liu |
| **链接** | https://openreview.net/forum?id=CkCFoN3j4s |

```bibtex
@misc{huang2025locret,
title={Locret: Enhancing Eviction in Long-Context {LLM} Inference with Trained Retaining Heads},
author={Yuxiang Huang and Binhang Yuan and Xu Han and Chaojun Xiao and Zhiyuan Liu},
year={2025},
url={https://openreview.net/forum?id=CkCFoN3j4s}
}
```

---

### 12. OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **作者** | (AntGroup) |
| **链接** | https://github.com/antgroup/OmniKV.git |

---

### 13. ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | (待检索) |
| **作者** | (待检索) |

---

## 三、KVCache调度与访问

### 14. MagicPIG: LSH Sampling for Efficient LLM Generation
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 (Spotlight) |
| **ID** | ALzTQUgW8a |
| **作者** | Zhuoming Chen, Ranajoy Sadhukhan, Zihao Ye, Yang Zhou, Jianyu Zhang, Niklas Nolte, Yuandong Tian, Matthijs Douze, Leon Bottou, Zhihao Jia, Beidi Chen |
| **链接** | https://openreview.net/forum?id=ALzTQUgW8a |
| **Affiliation** | Meta Facebook, Carnegie Mellon University, AI@INCITE |
| **Keywords** | locality sensitive hashing; randomized algorithms; LLM inference; KV cache |

```bibtex
@misc{chen2025magicpig,
title={MagicPIG: LSH Sampling for Efficient LLM Generation},
author={Zhuoming Chen and Ranajoy Sadhukhan and Zihao Ye and Yang Zhou and Jianyu Zhang and Niklas Nolte and Yuandong Tian and Matthijs Douze and Leon Bottou and Zhihao Jia and Beidi Chen},
year={2025},
url={https://openreview.net/forum?id=ALzTQUgW8a}
}
```

---

### 15. RetrievalAttention: Accelerating Long-Context LLM Inference via Vector Retrieval
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | qBpYqQUFPx |
| **作者** | Di Liu, Meng Chen, Baotong Lu, Huiqiang Jiang, Zhenhua Han, Qianxi Zhang, Qi Chen, Chengruidong Zhang, Bailu Ding, Kai Zhang, Chen Chen, Fan Yang, Yuqing Yang, Lili Qiu |
| **链接** | https://openreview.net/forum?id=qBpYqQUFPx |

```bibtex
@misc{liu2025retrievalattention,
title={RetrievalAttention: Accelerating Long-Context {LLM} Inference via Vector Retrieval},
author={Di Liu and Meng Chen and Baotong Lu and Huiqiang Jiang and Zhenhua Han and Qianxi Zhang and Qi Chen and Chengruidong Zhang and Bailu Ding and Kai Zhang and Chen Chen and Fan Yang and Yuqing Yang and Lili Qiu},
year={2025},
url={https://openreview.net/forum?id=qBpYqQUFPx}
}
```

---

### 16. ClusterGen: Token Generation in Sublinear Time and Memory with Clustering KV Cache
| 属性 | 内容 |
|------|------|
| **会议** | ICLR 2025 |
| **ID** | M922KJFO7O |
| **作者** | Amir Zandieh, Insu Han, Vahab Mirrokni, Amin Karbasi |
| **链接** | https://openreview.net/forum?id=M922KJFO7O |

```bibtex
@misc{zandieh2025clustergen,
title={ClusterGen: Token Generation in Sublinear Time and Memory with Clustering {KV} Cache},
author={Amir Zandieh and Insu Han and Vahab Mirrokni and Amin Karbasi},
year={2025},
url={https://openreview.net/forum?id=M922KJFO7O}
}
```

---

### 17. HiP: Hierarchically Pruned Attention
| 属性 | 内容 |
|------|------|
| **来源** | ICLR 2025 |
| **作者** | (待检索) |

---

### 18. KVMerger: KV Cache Merging Approach
| 属性 | 内容 |
|------|------|
| **来源** | ICLR 2025 |
| **作者** | (待检索) |

---

### 19. MPCache: MPC-friendly KV Cache Eviction
| 属性 | 内容 |
|------|------|
| **来源** | ICLR 2025 |
| **作者** | (待检索) |

---

### 20. VL-Cache: VLM-specific KV Cache Compression
| 属性 | 内容 |
|------|------|
| **来源** | ICLR 2025 |
| **作者** | (待检索) |

---

## 四、框架与系统

### 21. InfiniGen / RetrievalAttention / ShadowKV / HiP 系列
| 技术 | 说明 |
|------|------|
| **InfiniGen** | 无限上下文内存管理，CPU-based ANNS检索 |
| **ShadowKV** | 低秩Key + Value卸载，3.04x吞吐提升 |
| **HiP** | 分层剪枝注意力 + KV卸载 |
| **ParaDecode** | 中间层置信度并行解码 |

---

## 五、技术动态信源

### 框架Release (2026年)

| 框架 | 关键更新 |
|------|----------|
| **vLLM** | LoRA Weight Loading Overlap (TTFT降低78%), TRT-LLM NSA Kernel (DeepSeek V3.2 3-5x加速) |
| **SGLang v0.4+** | 精确多模态KV块哈希, KV Cache Manager v2, FlashInfer MLA后端 |

---

## 附录：顶会论文来源

| 会议 | 论文数量 | 数据库位置 |
|------|----------|------------|
| **ICML 2024** | ~2篇核心KV优化 | `2_AI情报织网\ai-intelligence-os\layers\data\conference_papers\icml2024.json` |
| **ICLR 2025** | ~15篇核心KV优化 | `2_AI情报织网\ai-intelligence-os\layers\data\conference_papers\iclr2025.json` |

---

*整理自Obsidian信息源*
*最后更新：2026-06-01*
