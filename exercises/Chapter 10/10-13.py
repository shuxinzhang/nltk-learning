# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★ Taking (Warren & Pereira, 1982) as a starting point, develop a technique
for converting a natural language query into a form that can be
evaluated more efficiently in a model. For example, given a query
of the form (P(x) & Q(x)), convert it to (Q(x) & P(x)) if
the extension of Q is smaller than the extension of
P.

'''