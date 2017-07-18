# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★ Use WordNet to create a semantic index for a text collection.
Extend the concordance search program in 3.6,
indexing each word using the offset of its first synset,
e.g. wn.synsets('dog')[0].offset (and optionally the
offset of some of its ancestors in the hypernym hierarchy).

'''