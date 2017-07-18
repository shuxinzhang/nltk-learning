# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★ Modify the functions init_wfst() and complete_wfst() so
that when a non-terminal symbol is added to a cell in the WFST, it includes
a record of the cells from which it was derived. Implement a
function that will convert a WFST in this form to a parse tree.

'''