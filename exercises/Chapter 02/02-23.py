# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
import math
'''
★ Zipf's Law:
Let f(w) be the frequency of a word w in free text. Suppose that
all the words of a text are ranked according to their frequency,
with the most frequent word first. Zipf's law states that the
frequency of a word type is inversely proportional to its rank
(i.e. f × r = k, for some constant k). For example, the 50th most
common word type should occur three times as frequently as the
150th most common word type.
Write a function to process a large text and plot word
frequency against word rank using pylab.plot. Do
you confirm Zipf's law? (Hint: it helps to use a logarithmic scale).
What is going on at the extreme ends of the plotted line?
Generate random text, e.g., using random.choice("abcdefg "),
taking care to include the space character.  You will need to
import random first.  Use the string
concatenation operator to accumulate characters into a (very)
long string.  Then tokenize this string, and generate the Zipf
plot as before, and compare the two plots.  What do you make of
Zipf's Law in the light of this?


'''
from nltk import FreqDist
import pylab
import numpy
from nltk.corpus import brown
def zipfProof(text):
	fdist = FreqDist([w.lower() for w in text])
	values = fdist.values()
	rankedValues = list(reversed(sorted(values)))
	x = []
	y = []
	for i in range(0,len(rankedValues)):
		rank = math.log10(i+1)
		freq = math.log10(rankedValues[i])
		x.append(rank)
		y.append(freq)
	rankavg = numpy.mean(x)
	freqavg = numpy.mean(y)
	pylab.plot(x,y)
	return pylab.show()

zipfProof(brown.words())



