# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Define a conditional frequency distribution over the Names corpus
that allows you to see which initial letters are more frequent for males
vs. females (cf. 4.4).
'''

from nltk import ConditionalFreqDist
from nltk.corpus import names
pair = [(gender,word[0]) for gender in names.fileids() for word in names.words(gender)]
print pair
cfd = ConditionalFreqDist(pair)
cfd.plot()