# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★ Use one of the predefined similarity measures to score
the similarity of each of the following pairs of words.
Rank the pairs in order of decreasing similarity.
How close is your ranking to the order given here,
an order that was established experimentally
by (Miller & Charles, 1998):
car-automobile, gem-jewel, journey-voyage, boy-lad,
coast-shore, asylum-madhouse, magician-wizard, midday-noon,
furnace-stove, food-fruit, bird-cock, bird-crane, tool-implement,
brother-monk, lad-brother, crane-implement, journey-car,
monk-oracle, cemetery-woodland, food-rooster, coast-hill,
forest-graveyard, shore-woodland, monk-slave, coast-forest,
lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string.
'''

from nltk.corpus import wordnet as wn

def similarity(word1,word2):
	max_ = 0
	synsetList1 = wn.synsets(word1)
	synsetList2 = wn.synsets(word2)
	for synset1 in synsetList1:
		for synset2 in synsetList2:
			if synset1.path_similarity(synset2) > max_:
				max_ = synset1.path_similarity(synset2)
	return max_

def rank(similarityList):
	return sorted(similarityList,key=lambda x:x[1], reverse = True)

def generate_similarity_list(pairList):
	similarityList = []
	for pair in pairList:
		similarity_pair = (pair,similarity(pair[0],pair[1]))
		similarityList.append(similarity_pair)
	return similarityList

def parse_data(string):
	pair = []
	stringList = string.split(', ')
	for str in stringList:
		wordPair = str.split('-');
		pair.append(wordPair)
	#print pair
	return pair


data = "car-automobile, gem-jewel, journey-voyage, boy-lad, coast-shore, asylum-madhouse, magician-wizard, midday-noon, furnace-stove, food-fruit, bird-cock, bird-crane, tool-implement, brother-monk, lad-brother, crane-implement, journey-car, monk-oracle, cemetery-woodland, food-rooster, coast-hill, forest-graveyard, shore-woodland, monk-slave, coast-forest, lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string"
print rank(generate_similarity_list(parse_data(data)))
