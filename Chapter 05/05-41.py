import nltk 
 '''
★
Develop an n-gram backoff tagger that permits "anti-n-grams" such as
["the", "the"] to be specified when a tagger is initialized.
An anti-ngram is assigned a count of zero and is used to prevent
backoff for this n-gram (e.g. to avoid
estimating P(the | the) as just P(the)).'''
