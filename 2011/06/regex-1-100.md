##匹配1-100的整数或包含两位小数的浮点数

##正则表达式一

        (?<!\d)(?:100|[1-9]\d?)(?!\d)(?:\.\d{2})?
测试结果(蓝色为匹配内容):       
<strong style="color:blue">1</strong>       
<strong style="color:blue">10</strong>      
<strong style="color:blue">100</strong>     
<strong style="color:blue">1.00</strong>        
<strong style="color:blue">100.00</strong>      
111     
<strong style="color:blue">100</strong>我       
你<strong style="color:blue">100</strong>你     
<strong style="color:blue">100.00</strong>0     

##正则表达式二

        (?<!\d)(?:100|[1-9]\d?)(?!\d)(?P<dot>\.\d{2}(?!\d))?(?(dot)|(?!\.))
        或
        (?<!\d)(?:100|[1-9]\d?)(?!\d)(\.\d{2}(?!\d))?(?(1)|(?!\.))
测试结果(蓝色为匹配内容):       
<strong style="color:blue">1</strong>       
<strong style="color:blue">10</strong>      
<strong style="color:blue">100</strong>     
<strong style="color:blue">1.00</strong>        
<strong style="color:blue">100.00</strong>      
111     
<strong style="color:blue">100</strong>我       
你<strong style="color:blue">100</strong>你     
100.000     

正则表达式二用到了条件语句。

        (?(id/name)...|...)
相当于 `if (id/name) ... else ...'      
示例：      
`a(b)?(?(1)c|d)'  匹配 abc 和 ad

###注意：作为条件的正则表达式一定要是一个可选的,即:
        (...)?

