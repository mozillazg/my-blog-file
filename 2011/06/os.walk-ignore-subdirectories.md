# os.walk 忽略某个目录下的子目录

##代码

<pre class="prettyprint">
import os

for root, dir, file in os.walk('./'):
    print root, dir, file
    dir[:] = [] # 忽略当前目录下的子目录
</pre>

##分析
为什么用`dir[:] = []` ,而不用`dir = []` ?

<pre class="prettyprint">
>>> a = [1, 2, 3]
>>> b = a  # b 与 a 指向同一个列表
>>> b
[1, 2, 3]
>>> id(a)
31247976
>>> id(b)
31247976
>>> b = [] # b 指向另一个列表
>>> b
[]
>>> a
[1, 2, 3]
>>> id(b)
31221680
>>> id(a)
31247976
>>> a = [1, 2, 3]
>>> b = a
>>> b[:] = []  # 或 del b[:] ,清空列表
>>> id(b)
31239624
>>> id(a)
31239624
>>> b
[]
>>> a
[]
</pre>

由上可知，使用`dir = []`并没有改变原来的列表，而`dir[:] = []`则是原地修改列表

