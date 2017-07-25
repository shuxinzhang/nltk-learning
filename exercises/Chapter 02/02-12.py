# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ The CMU Pronouncing Dictionary contains multiple pronunciations
for certain words.  How many distinct words does it contain?  What fraction
of words in this dictionary have more than one possible pronunciation?
'''

from nltk.corpus import cmudict
prondict = cmudict.words()
print len(prondict)
print len(set(prondict))
print -(len(set(prondict))-len(prondict))*1.0/len(prondict)

