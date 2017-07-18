# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ Sometimes a word is incorrectly tagged, e.g. the head noun in
"12/CD or/CC so/RB cases/VBZ".  Instead of requiring manual correction of
tagger output, good chunkers are able to work with the erroneous
output of taggers.  Look for other examples of correctly chunked
noun phrases with incorrect tags.
'''