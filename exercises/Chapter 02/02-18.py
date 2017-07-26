# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write a program to print the 50 most frequent bigrams
(pairs of adjacent words) of a text, omitting bigrams that contain stopwords.
'''
from nltk import FreqDist
from nltk.corpus import stopwords,words
def mostFrequentBigrams(text):
	stopwordsEng = stopwords.words('english')
	bigrams = nltk.bigrams(text)
	fq = FreqDist([(word1,word2) 
		for (word1,word2) in bigrams  
		if word1.lower() not in stopwordsEng and word1.isalpha()
		and word2.lower() not in stopwordsEng and word2.isalpha()])
	return fq.most_common(50)

print mostFrequentBigrams(nltk.corpus.brown.words(categories='news'))
print 'hello'

