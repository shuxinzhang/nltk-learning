# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★
Apply the n-gram and Brill tagging methods to IOB chunk tagging.
Instead of assigning POS tags to words, here we will assign IOB tags
to the POS tags.  E.g. if the tag DT (determiner) often occurs
at the start of a chunk, it will be tagged B (begin).  Evaluate
the performance of these chunking methods relative to the regular
expression chunking methods covered in this chapter.
'''