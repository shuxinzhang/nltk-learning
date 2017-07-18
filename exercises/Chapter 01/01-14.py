# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
import numpy as np
'''
☼ The first sentence of text3 is provided to you in the
variable sent3.  The index of the in sent3 is 1, because sent3[1]
gives us 'the'.  What are the indexes of the two other occurrences
of this word in sent3?

'''
from nltk.book import sent3
print sent3[1]
