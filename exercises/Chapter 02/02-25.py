# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★ Define a function find_language() that takes a string
as its argument, and returns a list of languages that have that
string as a word.  Use the udhr corpus and limit your searches
to files in the Latin-1 encoding.
'''
from nltk.corpus import udhr
def find_language(text):
	for fileid in udhr.fileids():
		if fileid[-6:] == "Latin1":
			if text in udhr.words(fileid):
				print (fileid[0:-7])
find_language("human")

