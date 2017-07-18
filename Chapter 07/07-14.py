# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★
The baseline chunker presented in the evaluation section tends to
create larger chunks than it should.  For example, the
phrase:
[every/DT time/NN] [she/PRP] sees/VBZ [a/DT newspaper/NN]
contains two consecutive chunks, and our baseline chunker will
incorrectly combine the first two: [every/DT time/NN she/PRP].
Write a program that finds which of these chunk-internal tags
typically occur at the start of a chunk, then
devise one or more rules that will split up these chunks.
Combine these with the existing baseline chunker and
re-evaluate it, to see if you have discovered an improved baseline.
'''