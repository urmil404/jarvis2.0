import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import dataset, dataloader

from NeauralNetwork import bag_of_words, tokenize, stem
from Brain import NeuralNet

with open("intents.json", "r") as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

for intent in intents["intents"]:
    tag = intent["tag"]
    tags.append(tag)

    for pattern in intent["patterns"]:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))  # must have to send set

ignore_words = [",", "?", "/", ".", "!"]
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(stem(set(all_words)))



