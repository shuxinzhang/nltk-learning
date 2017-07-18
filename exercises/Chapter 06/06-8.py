# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑
Word features can be very useful for performing document
classification, since the words that appear in a document give a
strong indication about what its semantic content is.  However,
many words occur very infrequently, and some of the most
informative words in a document may never have occurred in our
training data.  One solution is to make use of a lexicon,
which describes how different words relate to one another.  Using
WordNet lexicon, augment the movie review document classifier
presented in this chapter to use features that generalize the words
that appear in a document, making it more likely that they will
match words found in the training data.

'''