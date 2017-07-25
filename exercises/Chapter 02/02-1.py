# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk
'''
☼ Create a variable phrase containing a list of words.
Review the operations described in the previous chapter, including addition,
multiplication, indexing, slicing, and sorting.
'''

phrase = ['hello','world','this','is','shuxin']
# Addition, indexing and slicing
print phrase[0:1] + phrase[2:]
# Multiplication
print phrase * 2
# Sorting
print sorted(phrase)