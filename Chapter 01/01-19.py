# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ What is the difference between the following two lines?
Which one will give a larger value?  Will this be the case for other texts?

>>> sorted(set(w.lower() for w in text1))
>>> sorted(w.lower() for w in set(text1))
'''

'''
Second will give a larger value. 
'''