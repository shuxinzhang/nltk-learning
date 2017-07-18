# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★ The polysemy of a word is the number of senses it has.
Using WordNet, we can determine that the noun dog has 7 senses
with: len(wn.synsets('dog', 'n')).
Compute the average polysemy of nouns, verbs, adjectives and
adverbs according to WordNet.
'''