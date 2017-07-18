# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write expressions for finding all words in text6 that
meet the conditions listed below.  The result should be in the form of
a list of words: ['word1', 'word2', ...].

Ending in ize
Containing the letter z
Containing the sequence of letters pt
Having all lowercase letters except for an initial capital (i.e., titlecase)


'''

from nltk.book import text6
word_list = (w for w in text6 if (w.endswith('ize') and ('z' in w) and ('pt' in w) and (w.islower() or w.istitle())))
print list(word_list)