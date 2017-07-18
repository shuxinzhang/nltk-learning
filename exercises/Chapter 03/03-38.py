# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★ An interesting challenge for tokenization is words that have been
split across a line-break.  E.g. if long-term is split, then we
have the string long-\nterm.

Write a regular expression that identifies words that are
hyphenated at a line-break.  The expression will need to include the
\n character.
Use re.sub() to remove the \n character from these
words.
How might you identify words that should not remain hyphenated
once the newline is removed, e.g. 'encyclo-\npedia'?x


'''