# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write a program to create a table of word frequencies by genre,
like the one given in 1 for modals.
Choose your own words and try to find words whose presence
(or absence) is typical of a genre.  Discuss your findings.
'''

from nltk.corpus import brown
from nltk import ConditionalFreqDist

def frequency_table(words):
	cfd = ConditionalFreqDist([(genre,word)
		for genre in brown.categories()
		for word in brown.words(categories = genre)])
	genres = ['news','religion','hobbies','science_fiction','romance','humor']
	cfd.tabulate(conditions=genres,samples=words)

frequency_table(['America','love','dream'])