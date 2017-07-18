# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★ Write a program that processes a text and discovers
cases where a word has been used with a novel sense.
For each word, compute the WordNet similarity
between all synsets of the word and all synsets of the
words in its context.  (Note that this is a crude
approach; doing it well is a difficult, open research problem.)

'''