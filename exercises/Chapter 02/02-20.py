# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write a function word_freq() that takes a word and the name of a section
of the Brown Corpus as arguments, and computes the frequency of the word
in that section of the corpus.
'''

from nltk.corpus import brown
from nltk import FreqDist
def word_freq(word,section):
	fdist = FreqDist(brown.words(section))
	return fdist[word]

