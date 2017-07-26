# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write a function that finds the 50 most frequently occurring words
of a text that are not stopwords.
'''

from nltk.corpus import stopwords
from nltk import FreqDist;
def mostFrequent50(text):
	content = [w for w in text if w.isalpha() and w.lower() not in stopwords.words('english')]
	fd = FreqDist(content)
	return fd.most_common(50)

print mostFrequent50(nltk.corpus.brown.words(categories='romance'))
