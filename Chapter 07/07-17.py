# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★
An n-gram chunker can use information other than the current
part-of-speech tag and the n-1 previous chunk tags.
Investigate other models of the context, such as
the n-1 previous part-of-speech tags, or some combination of
previous chunk tags along with previous and following part-of-speech tags.
'''