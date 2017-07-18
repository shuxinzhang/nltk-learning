# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
★
The PP Attachment Corpus is a corpus describing
prepositional phrase attachment decisions.  Each instance in the
corpus is encoded as a PPAttachment object:




 

>>> from nltk.corpus import ppattach
>>> ppattach.attachments('training')
[PPAttachment(sent='0', verb='join', noun1='board',
              prep='as', noun2='director', attachment='V'),
 PPAttachment(sent='1', verb='is', noun1='chairman',
              prep='of', noun2='N.V.', attachment='N'),
 ...]
>>> inst = ppattach.attachments('training')[1]
>>> (inst.noun1, inst.prep, inst.noun2)
('chairman', 'of', 'N.V.')



Select only the instances where inst.attachment is N:




 

>>> nattach = [inst for inst in ppattach.attachments('training')
...            if inst.attachment == 'N']



Using this sub-corpus, build a classifier that attempts to predict
which preposition is used to connect a given pair of nouns.  For
example, given the pair of nouns "team" and "researchers," the
classifier should predict the preposition "of".  See the corpus
HOWTO at http://nltk.org/howto for more information on using the PP
attachment corpus.

'''