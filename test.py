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

from config import *
from prepareData import *
from models import *

encoder1=torch.load("save/enc.th")
attn_decoder1=torch.load("save/dec.th")
evaluateRandomly(encoder1, attn_decoder1)

















