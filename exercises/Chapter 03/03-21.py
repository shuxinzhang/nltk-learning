# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write a function unknown() that takes a URL as its argument,
and returns a list of unknown words that occur on that webpage.
In order to do this, extract all substrings consisting of lowercase letters
(using re.findall()) and remove any items from this set that occur
in the Words Corpus (nltk.corpus.words).  Try to categorize these words
manually and discuss your findings.

'''