# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Define a function supergloss(s) that takes a synset s as its argument
and returns a string consisting of the concatenation of the definition of s, and
the definitions of all the hypernyms and hyponyms of s.
'''
from nltk.corpus import wordnet as wn
def supergloss(s):
	description = s.definition()
	hypernyms = s.hypernyms()
	hypernyms_definition = ""
	for hypernym in hypernyms:
		hypernyms_definition = hypernym.definition() + "\n"

	hyponyms= s.hyponyms()
	hyponyms_definition = ""
	for hyponym in hyponyms:
		hyponyms_definition = hyponym.definition() + "\n"

	return description + "\n hypernyms: " + hypernyms_definition + "\n hyponyms: "+ hyponyms_definition

print supergloss(wn.synset('car.n.01'))
