# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Process each tree of the Treebank corpus sample nltk.corpus.treebank
and extract the productions with the help of Tree.productions().  Discard
the productions that occur only once.  Productions with the same left hand side,
and similar right hand sides can be collapsed, resulting in an equivalent but
more compact set of rules.  Write code to output a compact grammar.

'''