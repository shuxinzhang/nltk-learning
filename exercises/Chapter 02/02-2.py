# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ Use the corpus module to explore austen-persuasion.txt.
How many word tokens does this book have?  How many word types?
'''

from nltk.corpus import gutenberg
persuasion = gutenberg.raw('austen-persuasion.txt')
print len(persuasion)
print len(set(persuasion)) #word types: distinct words