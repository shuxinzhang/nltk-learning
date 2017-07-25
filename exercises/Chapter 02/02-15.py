# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write a program to find all words that occur at least three times in the Brown Corpus.
'''
from nltk.corpus import brown
from nltk import FreqDist
brown_words = [word.lower() for word in brown.words()]
fd = FreqDist(brown_words)
wordlist = []
for word in brown_words:
	if fd[word] > 3 and word.islower():
		wordlist.append(word)
print sorted(set(wordlist))