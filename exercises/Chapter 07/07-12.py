# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★
We saw in 5. that it is possible to establish
an upper limit to tagging performance by looking for ambiguous n-grams,
n-grams that are tagged in more than one possible way in the training data.
Apply the same method to determine an upper bound on the performance
of an n-gram chunker.
'''