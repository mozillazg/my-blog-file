##智能转换 bytes 为 kb/mb/gb/tb/pb...

用到了 math 模块中的一些函数

<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""智能转换 bytes 为 kb/mb/gb/tb/pb...
"""

import math

def convertBytes(bytes, lst=['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']):
    i = 0 if bytes == 0 else int(math.floor( # 舍弃小数点，取小
             math.log(bytes, 1024) # 求对数(对数：若 a**b = N 则 b 叫做以 a 为底 N 的对数)
            ))
    
    if i >= len(lst):
        i = len(lst) - 1
    return ('%.2f' + " " + lst[i]) % (bytes/math.pow(1024, i))

def main():
    lst = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    bytes = input('Bytes: ')
    print convertBytes(bytes, lst)

if __name__ == '__main__':
    main()
</pre>
