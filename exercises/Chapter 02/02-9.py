# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Pick a pair of texts and study the differences between them,
in terms of vocabulary, vocabulary richness, genre, etc.  Can you
find pairs of words which have quite different meanings across the
two texts, such as monstrous in Moby Dick and in Sense and Sensibility?
'''

from nltk.book import *
print text1.concordance('monstrous')
print text2.concordance('monstrous')
'''
Text1: "Monstrous" is usually used to mention that something has a large size.
Text2: "Monstrous" is used to indicate some emotions to a large extent.
'''

