# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ What percentage of noun synsets have no hyponyms?
You can get all noun synsets using wn.all_synsets('n').
'''

from nltk.corpus import wordnet as wn 
all_sets = wn.all_synsets('n')
total_count = 0;
no_hypo_count = 0;
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
for synset in all_sets:
	total_count+=1;
	if len(synset.hyponyms())==0:
		no_hypo_count+=1
print no_hypo_count*1.0/total_count
# 79.7% 