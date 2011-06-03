
python TypeError: 'int' object is not iterable

问题如何出现的，请看简单的示例：

<pre class="prettyprint">
>>> test = 10
>>> for i in test:
...    print i
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
</pre>

出错是因为 test 不是一个<span style="color:red; font-weight: blod;">序列或其他可迭代对象</span>。      
解决方案：

<pre class="prettyprint">
>>> test = [i for i in range(10)]
>>> test
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for i in test:
...    print i
...
0
1
2
3
4
5
6
7
8
9
</pre>
