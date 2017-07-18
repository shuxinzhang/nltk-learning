# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★
Our approach for tagging an unknown word has been to consider the letters of the word
(using RegexpTagger()), or to ignore the word altogether and tag
it as a noun (using nltk.DefaultTagger()).  These methods will not do well for texts having
new words that are not nouns.
Consider the sentence I like to blog on Kim's blog.  If blog is a new
word, then looking at the previous tag (TO versus NP$) would probably be helpful.
I.e. we need a default tagger that is sensitive to the preceding tag.
Create a new kind of unigram tagger that looks at the tag of the previous word,
and ignores the current word.  (The best way to do this is to modify the source
code for UnigramTagger(), which presumes knowledge of object-oriented
programming in Python.)
Add this tagger to the sequence of backoff taggers (including ordinary trigram
and bigram taggers that look at words), right before the usual default tagger.
Evaluate the contribution of this new unigram tagger.


'''