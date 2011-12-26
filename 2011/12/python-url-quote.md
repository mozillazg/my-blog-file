#[Python]使用 urllib.quote 进行 url 编码

python的url编码函数是在类urllib库中，使用方法是：

> urllib.quote(string[, safe])，除了三个符号“_.-”外，将所有符号编码，后面的参数safe是不编码的字符，使用的时候如果不设置的话，会将斜杠，冒号，等号，问号都给编码了。

    >>> import urllib
    >>> urllib.quote("a-b-c")
    'a-b-c'
    >>> urllib.quote("a+b+c")
    'a%2Bb%2Bc'
    >>> urllib.quote("http://test.com/a+b+c")
    'http%3A//test.com/a%2Bb%2Bc'
    >>> urllib.quote("http://test.com/a+b+c", ":/")
    'http://test.com/a%2Bb%2Bc'
    >>> urllib.quote("http://test.com/?q=a+b+c", ":?=/")
    'http://test.com/?q=a%2Bb%2Bc'

urllib2.quote 也是一样用法
