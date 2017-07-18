# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
from nltk import FreqDist
'''
◑ Find all the four-letter words in the Chat Corpus (text5).
With the help of a frequency distribution (FreqDist), show these
words in decreasing order of frequency.

'''

from nltk.book import text5
word_list = [w for w in text5 if len(w)==4]
fdist = FreqDist(word_list)
print fdist.most_common()