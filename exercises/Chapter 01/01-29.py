# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ We have been using sets to store vocabularies.  Try the following
Python expression: set(sent3) < set(text1).  Experiment with this using
different arguments to set().  What does it do?
Can you think of a practical application for this?

'''

from nltk.book import *
print set(sent3)<set(text1)
'''
return true if sent3's unique words is less than text1's unique words.
Compare two text's vocabulary size and determine if it is suitable for a particular group of people(e.g. kids)
'''