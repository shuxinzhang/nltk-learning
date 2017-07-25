# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ Investigate the holonym-meronym relations for some nouns.
Remember that there are three kinds of holonym-meronym relation,
so you need to use:
member_meronyms(), part_meronyms(), substance_meronyms(),
member_holonyms(), part_holonyms(), and substance_holonyms().
'''

from nltk.corpus import wordnet as wn

print wn.synsets('tree')
print wn.synset('tree.n.01').member_meronyms()
print wn.synset('tree.n.01').part_meronyms()
print wn.synset('tree.n.01').substance_meronyms()
print wn.synset('tree.n.01').member_holonyms()
print wn.synset('tree.n.01').part_holonyms()
print wn.synset('tree.n.01').substance_holonyms()