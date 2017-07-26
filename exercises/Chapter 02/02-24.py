#!/Users/shuxinzhang/.virtualenvs/nltk-learning/bin/python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
import sys
'''
★ Modify the text generation program in 2.2 further, to
do the following tasks:
Store the n most likely words in a list words then randomly
choose a word from the list using random.choice().  (You will need
to import random first.)
Select a particular genre, such as a section of the Brown Corpus,
or a genesis translation, one of the Gutenberg texts, or one of the Web texts.  Train
the model on this corpus and get it to generate random text.  You
may have to experiment with different start words. How intelligible
is the text?  Discuss the strengths and weaknesses of this method of
generating random text.
Now train your system using two distinct genres and experiment
with generating text in the hybrid genre.  Discuss your observations.


'''
import random
from nltk.corpus import brown
def random_generate_model(corpus, word, num=15):
	bigrams = nltk.bigrams(corpus)
	cfdist = nltk.ConditionalFreqDist(bigrams)
	for i in range(num):
		print (word, end=' ')
		wordList = cfdist[word].most_common(5)
		word = random.choice(wordList)[0]
	print()

text1 = brown.words(categories='romance')
text2 = brown.words(categories='news')
random_generate_model(text1,"The",30)
random_generate_model(text2,"The",30)

