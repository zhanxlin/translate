from __future__ import unicode_literals,print_function,division
from io import open
import unicodedata
import string
import re
import random
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

SOS_token = 0
EOS_token = 1

MAX_LENGTH = 10

eng_prefixes = (
    "i am ", "i m ",
    "he is", "he s ",
    "she is", "she s",
    "you are", "you re ",
    "we are", "we re ",
    "they are", "they re "
)

from prepareData import *
input_lang, output_lang, pairs = prepareData('eng', 'fra', True)
print(random.choice(pairs))

teacher_forcing_ratio = 0.5












