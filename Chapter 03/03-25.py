import nltk 
 '''
◑ Pig Latin is a simple transformation of English text.  Each word of the
text is converted as follows: move any consonant (or consonant cluster)
that appears at the start of the word to the end,
then append ay, e.g. string → ingstray,
idle → idleay.  http://en.wikipedia.org/wiki/Pig_Latin

Write a function to convert a word to Pig Latin.
Write code that converts text, instead of individual words.
Extend it further to preserve capitalization, to keep qu together
(i.e. so that quiet becomes ietquay), and to detect when y
is used as a consonant (e.g. yellow) vs a vowel (e.g. style).

'''
