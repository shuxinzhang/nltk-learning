# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★
As we saw in 7., it is possible
to collapse chunks down to their chunk label.  When we do this
for sentences involving the word gave, we find patterns
such as the following:

gave NP
gave up NP in NP
gave NP up
gave NP NP
gave NP to NP


Use this method to study the complementation patterns of a verb
of interest, and write suitable grammar productions.  (This task
is sometimes called lexical acquisition.)
Identify some English verbs that are near-synonyms, such as the
dumped/filled/loaded example from earlier in this chapter.
Use the chunking method to study the complementation patterns of
these verbs.  Create a grammar to cover these cases.  Can the verbs
be freely substituted for each other, or are their constraints?
Discuss your findings.


'''