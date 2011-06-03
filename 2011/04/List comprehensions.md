python 列表推导式   List comprehensions
 
<span style="color:red; font-weight: blod;">示例选自 </span>《Expert Python Programming》

 
未使用列表推导式：      
<pre class="prettyprint">
>>> numbers = range(10)
>>> size = len(numbers)
>>> evens = []
>>> i = 0
>>> while i < size:
...     if i % 2 == 0:
...         evens.append(i)
...     i += 1
...
>>> evens
[0, 2, 4, 6, 8]
</pre>
 
使用列表推导式：       
<pre class="prettyprint">
>>> [i for i in range(10) if i % 2 == 0]
[0, 2, 4, 6, 8]
</pre>
 
 
 
 


2.
def interval(start, stop=None, step=1):
    'imitates range()for step'
    if stop is None: #如果没有为stop提供值
        start, stop = 0,start #指定参数
    result = []
    i=start #计算start 索引
    while i< stop: #将索引添加到result内
        result.append(i)
        i += step #用step(>0)增加索引i
        
    return result 
    
    或： result = [i for i in range(start, stop)]
    