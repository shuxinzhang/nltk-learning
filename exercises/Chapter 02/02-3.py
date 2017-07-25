# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ Use the Brown corpus reader nltk.corpus.brown.words() or the Web text corpus
reader nltk.corpus.webtext.words() to access some sample text in two different genres.
'''

from nltk.corpus import brown,webtext
romance_text = brown.words(categories='romance')
print brown.categories()
print webtext.fileids()
print webtext.words('firefox.txt')