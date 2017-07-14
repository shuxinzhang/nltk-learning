import nltk 
 '''
◑ Readability measures are used to score the reading difficulty of a
text, for the purposes of selecting texts of appropriate difficulty
for language learners.  Let us define
μw to be the average number of letters per word, and
μs to be the average number of words per sentence, in
a given text.  The Automated Readability Index (ARI) of the text
is defined to be:
4.71 μw + 0.5 μs - 21.43.
Compute the ARI score for various sections of the Brown Corpus, including
section f (lore) and j (learned).  Make use of the fact that
nltk.corpus.brown.words() produces a sequence of words, while
nltk.corpus.brown.sents() produces a sequence of sentences.
'''
