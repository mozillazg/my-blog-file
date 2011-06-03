python  字符串批量替换  replace() translate() 

#替换单个字符#

##replace() 函数##

<pre class="prettyprint">
>>> from copy import deepcopy
>>> test = 'abc'
>>> d = {'a': 'A', 'b': 'B'}
>>> result = deepcopy(test)
>>> for i in d:
...     result = result.replace(i, d[i])
...     print result
...
Abc
ABc
>>> result
'ABc'
</pre>

##translate() 函数##

<pre class="prettyprint">
>>> from string import maketrans
>>> table = maketrans('ab', 'AB')
>>> test = 'abc'
>>> test.translate(table)
'ABc'
</pre>

# 替换多个字符 #    ----暂时不行，这两个函数做不到

<pre class="prettyprint">
>>> from string import maketrans
>>> a = 'abc'
>>> b = 'ABC'
>>> table = maketrans(a, b)
>>> 'abcd'.translate(table)
'ABCd'
>>>

>>> from string import maketrans
>>> a = 'abc'
>>> b = 'ABC'
>>> table = maketrans(a, b)
>>> 'abcd'.translate(table)
'ABCd'
>>> a = 'abcd'
>>> table = maketrans(a, b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: maketrans arguments must have same length
>>>

</pre>
