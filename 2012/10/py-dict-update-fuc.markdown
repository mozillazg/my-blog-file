a = dict()

a.update(b=3)
a
{'b': 3}

a.update('c'=4)
error
>>> a.update('b'='3')
  File "<stdin>", line 1
SyntaxError: keyword can't be an expression
>>>

a.update({'c': 4})
a
{'b': 3, 'c': 4}
