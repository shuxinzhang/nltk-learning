# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Define a function percent(word, text) that calculates
how often a given word occurs in a text, and expresses the result
as a percentage.

'''

def percent(word,text):
	return str(100*(text.count(word)/len(text)))+"%"