import nltk 
 '''
★
Consider the way an n-gram tagger uses recent tags to inform its tagging choice.
Now observe how a chunker may re-use this sequence information.  For example,
both tasks will make use of the information that nouns tend to follow adjectives
(in English).  It would appear that the same information is being maintained in
two places.  Is this likely to become a problem as the size of the rule sets grows?
If so, speculate about any ways that this problem might be addressed.'''
