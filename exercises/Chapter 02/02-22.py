# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Define a function hedge(text) which processes a
text and produces a new version with the word
'like' between every third word.
'''

def hedge(text):
	i = 3
	listText = list(text)
	while i < len(text):
		listText.insert(i,'like')
		i += 4 
	return listText

# print nltk.corpus.brown.fileids()
print hedge(nltk.corpus.brown.words('ca01'))