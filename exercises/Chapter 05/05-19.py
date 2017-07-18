# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑ The evaluate() method works out how accurately
the tagger performs on this text.  For example, if the supplied tagged text
was [('the', 'DT'), ('dog', 'NN')] and the tagger produced the output
[('the', 'NN'), ('dog', 'NN')], then the score would be 0.5.
Let's try to figure out how the evaluation method works:
A tagger t takes a list of words as input, and produces a list of tagged words
as output.  However, t.evaluate() is given correctly tagged text as its only parameter.
What must it do with this input before performing the tagging?
Once the tagger has created newly tagged text, how might the evaluate() method
go about comparing it with the original tagged text and computing the accuracy score?
Now examine the source code to see how the method is implemented.  Inspect
nltk.tag.api.__file__ to discover the location of the source code,
and open this file using an editor (be sure to use the api.py file and
not the compiled api.pyc binary file).


'''