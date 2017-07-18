# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ Consider the following statements:




 

>>> read_expr = nltk.sem.Expression.fromstring
>>> e2 = read_expr('pat')
>>> e3 = nltk.sem.ApplicationExpression(e1, e2)
>>> print(e3.simplify())
exists y.love(pat, y)



Clearly something is missing here, namely a declaration of the
value of e1. In order for ApplicationExpression(e1, e2)
to be β-convertible to exists y.love(pat, y), e1
must be a λ-abstract which can take pat as an
argument. Your task is to construct such an abstract, bind it to
e1, and satisfy yourself that the statements above are all
satisfied (up to alphabetic variance). In addition, provide an
informal English translation of e3.simplify().
Now carry on doing this same task for the further cases of
e3.simplify() shown below.




 

>>> print(e3.simplify())
exists y.(love(pat,y) | love(y,pat))







 

>>> print(e3.simplify())
exists y.(love(pat,y) | love(y,pat))







 

>>> print(e3.simplify())
walk(fido)




'''