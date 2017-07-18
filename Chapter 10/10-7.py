# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ As in the preceding exercise, find a λ abstract e1 that yields
results equivalent to those shown below.




 

>>> e2 = read_expr('bark')
>>> e3 = nltk.sem.ApplicationExpression(e1, e2)
>>> print(e3.simplify())
exists y.(dog(x) & bark(x))







 

>>> e2 = read_expr('bark')
>>> e3 = nltk.sem.ApplicationExpression(e1, e2)
>>> print(e3.simplify())
bark(fido)







 

>>> e2 = read_expr('\\P. all x. (dog(x) -> P(x))')
>>> e3 = nltk.sem.ApplicationExpression(e1, e2)
>>> print(e3.simplify())
all x.(dog(x) -> bark(x))




'''