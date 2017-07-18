# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ We saw a method for discovering cases of whole-word reduplication.
Write a function to find words that may contain partial
reduplication.  Use the re.search() method, and the following
regular expression: (..+)\1

'''