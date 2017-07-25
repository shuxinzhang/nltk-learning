# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Write a program to generate a table of lexical diversity scores (i.e. token/type ratios), as we saw in
1.1.  Include the full set of Brown Corpus genres (nltk.corpus.brown.categories()).
Which genre has the lowest diversity (greatest number of tokens per type)?
Is this what you would have expected?
'''
from nltk.corpus import brown
def lexical_diversity(text):
	return len(set(text))*1.0/len(text)

for genre in brown.categories():
	print genre + ":" + str(lexical_diversity(brown.words(categories = genre)))





