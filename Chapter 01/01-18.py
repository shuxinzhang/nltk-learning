# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Using list addition, and the set and sorted operations, compute the
vocabulary of the sentences sent1 ... sent8.

'''

from nltk.book import *

sentences = sent1+sent2+sent3+sent4+sent5+sent6+sent7+sent8
print sorted(set(sentences))