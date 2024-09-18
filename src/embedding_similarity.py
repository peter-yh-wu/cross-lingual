#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2024 Peter Wu
#  Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0)

"""Compute the cosine similarity between two waveforms.
"""

import numpy as np
import os
import s3prl.hub as hub
import librosa
import torch

from tqdm import tqdm

model_name = 'xlsr_53'
model = getattr(hub, model_name)() 
device = 'cpu'
model = model.to(device)
layer_num = 9

file1 = '/path/to/language_1_audio_file.wav'
file2 = '/path/to/language_2_audio_file.wav'
features = []
with torch.no_grad():
    for file in [file1, file2]:
        a, sr = librosa.load(file, sr=16000)
        wavs = [torch.from_numpy(a).float().to(device)]
        states = model(wavs)["hidden_states"]
        feature = states[layer_num].squeeze(0)
        feature = feature.mean(0)
        features.append(feature)
sim = torch.nn.functional.cosine_similarity(features[0].unsqueeze(0), features[1].unsqueeze(0))
