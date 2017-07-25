# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ Read in the texts of the State of the Union addresses, using the
state_union corpus reader.  Count occurrences of men, women,
and people in each document.  What has happened to the usage of these
words over time?
'''

from nltk.corpus import state_union
#print state_union.fileids()
targets = ['men','women','people']
pair = [(target,fileid[:4]) for fileid in state_union.fileids() for word in state_union.words(fileid) for target in targets if word.lower()==target]
print pair
cfd = nltk.ConditionalFreqDist(pair)
cfd.plot()