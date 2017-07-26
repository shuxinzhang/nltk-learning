# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write a program to guess the number of syllables contained in a text,
making use of the CMU Pronouncing Dictionary.
'''

from nltk.corpus import cmudict
from nltk.corpus import brown
def countSyllables(text):
	prondict = cmudict.dict()
	count = 0
	for word in text:
		if word.isalpha():
			if word in prondict:
				count = count + len(prondict[word.lower()])
			else :
				count += 2 # Average syllable per english word
	return count
print countSyllables(brown.words(categories = 'news'))
