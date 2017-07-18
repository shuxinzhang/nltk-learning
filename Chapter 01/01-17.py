# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Use text9.index() to find the index of the word sunset.
You'll need to insert this word as an argument between the parentheses.
By a process of trial and error, find the slice for the complete sentence that
contains this word.

'''
from nltk.book import text9
print text9.index('sunset')
print text9[621:644]