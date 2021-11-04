# Cross-lingual Transfer for Speech Processing using Acoustic Language Similarity

Indic TTS Samples can be found at [https://peter-yh-wu.github.io/cross-lingual/](https://peter-yh-wu.github.io/cross-lingual/)

Code for neural ASR & TTS experiments can be found at [https://github.com/peter-yh-wu/espnet](https://github.com/peter-yh-wu/espnet)

 - The [javanese_asr](https://github.com/peter-yh-wu/espnet/tree/javanese_asr) branch contains scripts to train the Javanese ASR model in `egs2/java`
 - The [sundanese_asr](https://github.com/peter-yh-wu/espnet/tree/sundanese_asr) branch contains scripts to train the Sundanese ASR model in `egs2/sunda`
 - The [indic_tts](https://github.com/peter-yh-wu/espnet/tree/indic_tts) branch contains scripts to train the Indic TTS models in `egs/cmu_indic`
 
 The `embs/` directory contains our acoustic-based language embeddings, where each index corresponds to the respective language in `language_ids.txt`. [LangList.txt](https://github.com/festvox/datasets-CMU_Wilderness/blob/master/LangList.txt) contains more details about each language.

## Paper

[**Cross-lingual Transfer for Speech Processing using Acoustic Language Similarity**](https://arxiv.org/abs/2111.01326)

```
@inproceedings{wu2021crosslingual,
      title={Cross-lingual Transfer for Speech Processing using Acoustic Language Similarity},
      author={Peter Wu and Jiatong Shi and Yifan Zhong and Shinji Watanabe and Alan W Black},
      booktitle={ASRU},
      year={2021}
}
```
