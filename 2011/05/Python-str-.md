偶然看到论坛有人问python字符串怎么没有反转的方法，是很纳闷。后来找到了几个解决办法，还是很酷的说，记录以分享下。

>>> s = "abcdefg"

1.
>>> s[::-1]

2.
>>> a=list(s)
>>> a.reverse()
>>> "".join(a)

3.
>>> reduce(lambda x,y:y+x,s)


1和3都很酷，也有python特色，2则是折中的一个土办法、


a='hello,world' b=a[::-1]

反转单词的最简单方法

a='hello world' ' '.join(a.split( )[::-1])

注：这种方式会将单词间的多个空格合并为一个空格要保留这些空格的化，使用正则表达式 import re revwords = re.split(r'(\s+)', astring) # separators too, since '(...)' revwords.reverse( ) # reverse the list in place revwords = ''.join(revwords) # list of strings -> string 以上三行也可以写成一行，不过可读性就差多了 revwords = ''.join(re.split(r'(\s+)', astring)[::-1]) 如果你用的是python2.4,你可以用新增的reversed函数来使上面这个单行语句更可读 revwords = ''.join(reversed(re.split(r'(\s+)', astring))) 不过对于逐字符翻转来说，虽然[::-1]很难读，它仍然是最有效率的方法，reversed()返回的是一个iterator (迭代)对象，不是字符串，所以必须得用''.join连接一下才可读。

-- 

假设有字符串"s"，如下方法进行反转（下面是在iPython中的输入输出）：

In [1]: s='123456789'

In [2]: s

Out[2]: '123456789'

In [3]: s[::-1]

Out[3]: '987654321'

In [4]: reduce(lambda x,y:y+x,s)

Out[4]: '987654321'

In [5]: x=list(s); x.reverse(); "".join(x)

Out[5]: '987654321'