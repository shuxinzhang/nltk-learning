# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ Review the discussion of conditionals in 4.
Find all words in the Chat Corpus (text5)
starting with the letter b.  Show them in alphabetical order.

'''
from nltk.book import text5
word_list = sorted(w for w in set(text5) if w.startswith('b'))
print word_list