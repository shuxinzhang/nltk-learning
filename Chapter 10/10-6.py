import nltk 
 '''
☼ As in the preceding exercise, find a λ abstract e1 that yields
results equivalent to those shown below.




 

>>> e2 = read_expr('chase')
>>> e3 = nltk.sem.ApplicationExpression(e1, e2)
>>> print(e3.simplify())
\x.all y.(dog(y) -> chase(x,pat))







 

>>> e2 = read_expr('chase')
>>> e3 = nltk.sem.ApplicationExpression(e1, e2)
>>> print(e3.simplify())
\x.exists y.(dog(y) & chase(pat,x))







 

>>> e2 = read_expr('give')
>>> e3 = nltk.sem.ApplicationExpression(e1, e2)
>>> print(e3.simplify())
\x0 x1.exists y.(present(y) & give(x1,y,x0))



'''
