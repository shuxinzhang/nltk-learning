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
from nltk.corpus import wordnet as wn
def polysemy_calc(type):
	total = 0
	polysemy_count = 0

	for synset in wn.all_synsets():
		if synset.pos() == type:
			for lemma in synset.lemmas():
				total += 1
				polysemy_count += polysemy(lemma.name(),synset.pos())

	return polysemy_count*1.0/total

def polysemy(name , pos):
	count = 0
	count += len(wn.synsets(name,pos))
	return count
#print (polysemy('dog','n'))
print ("noun:"+str(polysemy_calc('n')))
print ("verb:"+str(polysemy_calc('v')))
print ("Adjectives:"+str(polysemy_calc('a')))