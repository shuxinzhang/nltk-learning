# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Define sent to be the list of words
['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'].
Now write code to perform the following tasks:

Print all words beginning with sh
Print all words longer than four characters


'''

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print list(word for word in sent if word.startswith('sh'))
print list(word for word in sent if len(word)>4)