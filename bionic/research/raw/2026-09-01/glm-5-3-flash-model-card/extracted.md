#  [ ](<https://huggingface.co/zai-org/GLM-5.3-Flash#glm-53-flash>) GLM-5.3-Flash 

![](logo-bce1dbb2.svg)

👋 Join our [WeChat](<https://raw.githubusercontent.com/zai-org/GLM-5/refs/heads/main/resources/wechat.png>) or [Discord](<https://discord.gg/QR7SARHRxK>) community.   
📖 Check out the GLM-5.3-Flash [blog](<https://z.ai/blog/glm-5.3-flash>) and GLM-5 [Technical report](<https://arxiv.org/abs/2602.15763>).   
📍 Use GLM-5.3-Flash API services on [Z.ai API Platform. ](<https://docs.z.ai/guides/llm/glm-5.3-flash>)

##  [ ](<https://huggingface.co/zai-org/GLM-5.3-Flash#introduction>) Introduction 

We introduce GLM-5.3-Flash, the first natively multimodal model in the GLM-5 series. With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks and real-world workloads at one-tenth the price, while approaching Claude Opus 4.8 on coding and agentic benchmarks.

GLM-5.3-Flash starts from a newly trained base model, with its architecture and training recipe redesigned around capability and efficiency. For the first time in the GLM series, we introduce a hybrid architecture combining sparse and linear attention, sharply reducing long-context serving costs while preserving precise long-context capabilities. The model also adopts Manifold-Constrained Hyper-Connections (mHC) to further improve scaling efficiency. Together with our latest 30T-token multimodal pre-training corpus, these changes enable GLM-5.3-Flash to deliver more intelligence with less compute.

[![bench_53](bench_53-c52678c7.png)](<https://raw.githubusercontent.com/zai-org/GLM-5/refs/heads/main/resources/bench_53.png>)

##  [ ](<https://huggingface.co/zai-org/GLM-5.3-Flash#serve-glm-53-flash-locally>) Serve GLM-5.3-Flash Locally 

GLM-5.3-Flash supports deployment with the following frameworks. Feel free to try them out:

  * [SGLang](<https://github.com/sgl-project/sglang>) — see [cookbook](<https://cookbook.sglang.io/autoregressive/GLM/GLM-5.3-Flash>)
  * [vLLM](<https://github.com/vllm-project/vllm>) — see [recipes](<https://recipes.vllm.ai/zai-org/GLM-5.3-Flash>)
  * [TokenSpeed](<https://github.com/lightseekorg/tokenspeed>) — see [here](<https://lightseek.org/tokenspeed/recipes/models#glm-5-3-flash>)
  * [Transformers](<https://github.com/huggingface/transformers>) — see [transformers docs](<https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/glm5_next.md>)
  * [KTransformers](<https://github.com/kvcache-ai/ktransformers>) — see [tutorial](<https://github.com/kvcache-ai/ktransformers/blob/main/doc/en/kt-kernel/GLM-5.3-Flash-Tutorial.md>)
  * [Unsloth](<https://github.com/unslothai/unsloth>) — see [guide](<https://unsloth.ai/docs/models/glm-5.3>)

###  [ ](<https://huggingface.co/zai-org/GLM-5.3-Flash#note>) Note 

  * GLM-5.3-Flash supports controlling the thinking budget through the `reasoning_effort` parameter, which accepts three levels: `low`, `high`, and `max`. It defaults to `max` if not passed (or if set to any other value). To use `low` or `high`, pass them explicitly. For benchmark and leaderboard reproduction, keep the default `max`.
  * In the chat template for GLM-5.3-Flash, `clear_thinking` defaults to `false` if not passed. For chat scenarios, explicitly pass `clear_thinking=true`.

##  [ ](<https://huggingface.co/zai-org/GLM-5.3-Flash#footnotes>) Footnotes 

  * **HLE w/ tools (full set)** : We use sampling parameters of `temperature=1.0` and `top_p=0.95` for evaluation, with a maximum generation length of `163,840` tokens. The evaluation is conducted with a maximum context length of `300,000` tokens, using a context management strategy. We use GPT-5.6-luna (medium) as the judge model.
  * **NL2Repo** : We evaluated NL2Repo with temperature=1.0, top_p=1.0, and max_new_tokens=64k under 1M context. To prevent hacking, we use rule-based and a LLM-based judgement to prevent malicious behaviors (e.g., unauthorized pip or curl operations).
  * **DeepSWE** : We run DeepSWE using the mini-swe-agent harness with `temperature=0.95`, `top_p=1.0`, `timeout=6h` and 400K context.
  * **Terminal-Bench 2.1** : We evaluate in Claude Code 2.1.207 with temperature=1.0, top_p=1, max_new_tokens=65536 with 6h timeout.
  * **Agent’s Last Exam** : 
  * **Toolathlon Verified** : We obtain all results via the official evaluation service and report pass@1 averaged over 3 independent runs.
  * **AutomationBench** : We evaluate on AutomationBench **v1.0.6** , incorporating the fix for the `null`-type handling issue introduced in [PR #13](<https://github.com/zapier/AutomationBench/pull/13>).
  * **GDPval-AA v2** : Models are evaluated by Artificial Analysis.
  * **BabyVision** : We use temperature=1.0, top_p=0.95, and a maximum context length of 164K tokens. We resize the input images such that their shorter side is at least 1.5K pixels, consistent with other baselines.

##  [ ](<https://huggingface.co/zai-org/GLM-5.3-Flash#citation>) Citation 

If you find GLM-5.3-Flash useful in your research, please cite our technical report:

```bibtex
@misc{glm5team2026glm5vibecodingagentic,
      title={GLM-5: from Vibe Coding to Agentic Engineering},
      author={GLM-5-Team and : and Aohan Zeng and Xin Lv and Zhenyu Hou and Zhengxiao Du and Qinkai Zheng and Bin Chen and Da Yin and Chendi Ge and Chenghua Huang and Chengxing Xie and Chenzheng Zhu and Congfeng Yin and Cunxiang Wang and Gengzheng Pan and Hao Zeng and Haoke Zhang and Haoran Wang and Huilong Chen and Jiajie Zhang and Jian Jiao and Jiaqi Guo and Jingsen Wang and Jingzhao Du and Jinzhu Wu and Kedong Wang and Lei Li and Lin Fan and Lucen Zhong and Mingdao Liu and Mingming Zhao and Pengfan Du and Qian Dong and Rui Lu and Shuang-Li and Shulin Cao and Song Liu and Ting Jiang and Xiaodong Chen and Xiaohan Zhang and Xuancheng Huang and Xuezhen Dong and Yabo Xu and Yao Wei and Yifan An and Yilin Niu and Yitong Zhu and Yuanhao Wen and Yukuo Cen and Yushi Bai and Zhongpei Qiao and Zihan Wang and Zikang Wang and Zilin Zhu and Ziqiang Liu and Zixuan Li and Bojie Wang and Bosi Wen and Can Huang and Changpeng Cai and Chao Yu and Chen Li and Chengwei Hu and Chenhui Zhang and Dan Zhang and Daoyan Lin and Dayong Yang and Di Wang and Ding Ai and Erle Zhu and Fangzhou Yi and Feiyu Chen and Guohong Wen and Hailong Sun and Haisha Zhao and Haiyi Hu and Hanchen Zhang and Hanrui Liu and Hanyu Zhang and Hao Peng and Hao Tai and Haobo Zhang and He Liu and Hongwei Wang and Hongxi Yan and Hongyu Ge and Huan Liu and Huanpeng Chu and Jia'ni Zhao and Jiachen Wang and Jiajing Zhao and Jiamin Ren and Jiapeng Wang and Jiaxin Zhang and Jiayi Gui and Jiayue Zhao and Jijie Li and Jing An and Jing Li and Jingwei Yuan and Jinhua Du and Jinxin Liu and Junkai Zhi and Junwen Duan and Kaiyue Zhou and Kangjian Wei and Ke Wang and Keyun Luo and Laiqiang Zhang and Leigang Sha and Liang Xu and Lindong Wu and Lintao Ding and Lu Chen and Minghao Li and Nianyi Lin and Pan Ta and Qiang Zou and Rongjun Song and Ruiqi Yang and Shangqing Tu and Shangtong Yang and Shaoxiang Wu and Shengyan Zhang and Shijie Li and Shuang Li and Shuyi Fan and Wei Qin and Wei Tian and Weining Zhang and Wenbo Yu and Wenjie Liang and Xiang Kuang and Xiangmeng Cheng and Xiangyang Li and Xiaoquan Yan and Xiaowei Hu and Xiaoying Ling and Xing Fan and Xingye Xia and Xinyuan Zhang and Xinze Zhang and Xirui Pan and Xu Zou and Xunkai Zhang and Yadi Liu and Yandong Wu and Yanfu Li and Yidong Wang and Yifan Zhu and Yijun Tan and Yilin Zhou and Yiming Pan and Ying Zhang and Yinpei Su and Yipeng Geng and Yong Yan and Yonglin Tan and Yuean Bi and Yuhan Shen and Yuhao Yang and Yujiang Li and Yunan Liu and Yunqing Wang and Yuntao Li and Yurong Wu and Yutao Zhang and Yuxi Duan and Yuxuan Zhang and Zezhen Liu and Zhengtao Jiang and Zhenhe Yan and Zheyu Zhang and Zhixiang Wei and Zhuo Chen and Zhuoer Feng and Zijun Yao and Ziwei Chai and Ziyuan Wang and Zuzhou Zhang and Bin Xu and Minlie Huang and Hongning Wang and Juanzi Li and Yuxiao Dong and Jie Tang},
      year={2026},
      eprint={2602.15763},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2602.15763},
}
```

Downloads last month
    441,348

Safetensors[](<https://huggingface.co/docs/safetensors>)

Model size

321B params

Tensor type

BF16 

·

F8_E4M3 

·

F32 

·

Chat template

Files info

##  Model tree for zai-org/GLM-5.3-Flash [](<https://huggingface.co/docs/hub/model-cards#specifying-a-base-model>)

Adapters

[1 model](<https://huggingface.co/models?other=base_model:adapter:zai-org/GLM-5.3-Flash>)

Finetunes

[11 models](<https://huggingface.co/models?other=base_model:finetune:zai-org/GLM-5.3-Flash>)

Merges

[1 model](<https://huggingface.co/models?other=base_model:merge:zai-org/GLM-5.3-Flash>)

Quantizations

[](<https://huggingface.co/models?apps=llama.cpp&other=base_model:quantized:zai-org/GLM-5.3-Flash> "Use with llama.cpp")[](<https://huggingface.co/models?apps=lmstudio&other=base_model:quantized:zai-org/GLM-5.3-Flash> "Use with LM Studio")[](<https://huggingface.co/models?apps=jan&other=base_model:quantized:zai-org/GLM-5.3-Flash> "Use with Jan")[](<https://huggingface.co/models?apps=ollama&other=base_model:quantized:zai-org/GLM-5.3-Flash> "Use with Ollama")

[80 models](<https://huggingface.co/models?other=base_model:quantized:zai-org/GLM-5.3-Flash>)

##  Spaces using zai-org/GLM-5.3-Flash 5

##  Collection including zai-org/GLM-5.3-Flash

[ 4 items • Updated 5 days ago • 32](<https://huggingface.co/collections/zai-org/glm-53>)

##  Paper for zai-org/GLM-5.3-Flash

[ Paper • 2602.15763 • Published Feb 17 • 217 ](<https://huggingface.co/papers/2602.15763>)

##  Evaluation results [](<https://huggingface.co/docs/hub/eval-results>)

  * [llamaindex/ExtractBench](<https://huggingface.co/datasets/llamaindex/ExtractBench>) [leaderboard ](<https://huggingface.co/datasets/llamaindex/ExtractBench?eval_result=zai-org/GLM-5.3-Flash>)
  * Mean [View evaluation results ](<https://huggingface.co/zai-org/GLM-5.3-Flash/discussions/29>) [![](F5Z_0zjcdl0cIKIq-MvTR-eb26d6b2.jpeg) source](<https://huggingface.co/datasets/llamaindex/ExtractBench>)

Pipeline name: glm_5_3_flash_extract_oneshot_structured_output_file

80.75 *

  * Short [View evaluation results ](<https://huggingface.co/zai-org/GLM-5.3-Flash/discussions/29>) [![](F5Z_0zjcdl0cIKIq-MvTR-eb26d6b2.jpeg) source](<https://huggingface.co/datasets/llamaindex/ExtractBench>)

Pipeline name: glm_5_3_flash_extract_oneshot_structured_output_file

[](<https://huggingface.co/datasets/llamaindex/ExtractBench?eval_result=zai-org%2FGLM-5.3-Flash&leaderboard_task_id=short>) 96.3 *

  * Medium [View evaluation results ](<https://huggingface.co/zai-org/GLM-5.3-Flash/discussions/29>) [![](F5Z_0zjcdl0cIKIq-MvTR-eb26d6b2.jpeg) source](<https://huggingface.co/datasets/llamaindex/ExtractBench>)

Pipeline name: glm_5_3_flash_extract_oneshot_structured_output_file

51.56 *

  * +1 more
  * [harborframework/terminal-bench-2.1](<https://huggingface.co/datasets/harborframework/terminal-bench-2.1>) · Terminalbench 2 1 [View evaluation results ](<https://huggingface.co/zai-org/GLM-5.3-Flash/discussions/12>) [leaderboard ](<https://huggingface.co/datasets/harborframework/terminal-bench-2.1?eval_result=zai-org/GLM-5.3-Flash&leaderboard_task_id=terminalbench_2_1>)

[](<https://huggingface.co/datasets/harborframework/terminal-bench-2.1?eval_result=zai-org%2FGLM-5.3-Flash&leaderboard_task_id=terminalbench_2_1&leaderboard_max_params=500B>) 84.3

  * [datacurve/deep-swe](<https://huggingface.co/datasets/datacurve/deep-swe>) · Deep Swe [View evaluation results ](<https://huggingface.co/zai-org/GLM-5.3-Flash/discussions/12>) [leaderboard ](<https://huggingface.co/datasets/datacurve/deep-swe?eval_result=zai-org/GLM-5.3-Flash&leaderboard_task_id=deep_swe>)

[](<https://huggingface.co/datasets/datacurve/deep-swe?eval_result=zai-org%2FGLM-5.3-Flash&leaderboard_task_id=deep_swe&leaderboard_max_params=500B>) 63.4 *

Expand 2 benchmarks
