# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑
We defined the regexp_tagger that can be used
as a fall-back tagger for unknown words.  This tagger only checks for
cardinal numbers.  By testing for particular prefix or suffix strings,
it should be possible to guess other tags.  For example,
we could tag any word that ends with -s as a plural noun.
Define a regular expression tagger (using RegexpTagger())
that tests for at least five other patterns in the spelling of words.
(Use inline documentation to explain the rules.)
'''