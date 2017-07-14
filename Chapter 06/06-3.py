import nltk 
 '''
☼ The Senseval 2 Corpus contains data intended to train
word-sense disambiguation classifiers.  It contains data for
four words: hard, interest, line, and serve.  Choose one of these
four words, and load the corresponding data:




 

>>> from nltk.corpus import senseval
>>> instances = senseval.instances('hard.pos')
>>> size = int(len(instances) * 0.1)
>>> train_set, test_set = instances[size:], instances[:size]



Using this dataset, build a classifier that predicts the correct
sense tag for a given instance.  See the corpus HOWTO at
http://nltk.org/howto for information on using the instance objects
returned by the Senseval 2 Corpus.
'''
