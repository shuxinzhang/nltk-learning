# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼
Save some text into a file corpus.txt.  Define a function load(f)
that reads from the file named in its sole argument, and returns a string
containing the text of the file.

Use nltk.regexp_tokenize() to create a tokenizer that tokenizes
the various kinds of punctuation in this text.  Use one multi-line
regular expression, with inline comments, using the verbose flag (?x).
Use nltk.regexp_tokenize() to create a tokenizer that tokenizes
the following kinds of expression: monetary amounts; dates; names
of people and organizations.


'''