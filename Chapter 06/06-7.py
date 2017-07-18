# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
◑
The dialog act classifier assigns labels to individual posts,
without considering the context in which the post is found.
However, dialog acts are highly dependent on context, and some
sequences of dialog act are much more likely than others.  For
example, a ynQuestion dialog act is much more likely to be
answered by a yanswer than by a greeting.  Make use of this
fact to build a consecutive classifier for labeling dialog acts.
Be sure to consider what features might be useful.  See the code
for the consecutive classifier for part-of-speech tags in
1.7 to get some ideas.

'''