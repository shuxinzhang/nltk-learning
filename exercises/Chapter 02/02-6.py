# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ In the discussion of comparative wordlists, we created an object
called translate which you could look up using words in both German and Spanish
in order to get corresponding words in English.
What problem might arise with this approach?
Can you suggest a way to avoid this problem?
'''

'''
some words with multiple meanings might cause ambiguity.
Compare the synset of the two words, compare the synonyms and get words along with definitions with the closest meaning.
'''
