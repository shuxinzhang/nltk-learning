import nltk 
 '''
★
The Penn Treebank contains a section of tagged Wall Street Journal text
that has been chunked into noun phrases.  The format uses square brackets,
and we have encountered it several times during this chapter.
The Treebank corpus can be accessed using:
for sent in nltk.corpus.treebank_chunk.chunked_sents(fileid).  These are flat trees,
just as we got using nltk.corpus.conll2000.chunked_sents().
The functions nltk.tree.pprint() and nltk.chunk.tree2conllstr()
can be used to create Treebank and IOB strings from a tree.
Write functions chunk2brackets() and chunk2iob() that take a single
chunk tree as their sole argument, and return the required multi-line string
representation.
Write command-line conversion utilities bracket2iob.py and iob2bracket.py
that take a file in Treebank or CoNLL format (resp) and convert it to the other
format.  (Obtain some raw Treebank or CoNLL data from the NLTK Corpora, save it
to a file, and then use for line in open(filename) to access it from Python.)

'''
