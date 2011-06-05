
这个脚本的功能如下：      
移动文件到由最后修改日期组成的目录下    
例如：test.txt 创建于 2011/06/03, 那么它将被移动到 2011/06 目录下

<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""移动文件到相应日期目录下。
例如：test.txt 最后修改时间：2011/06/03
移动到目录 2011/06 下
"""

import os
import time

def move_file(file_path):
    """移动文件到相应的日期目录下
    """
    if os.path.isdir(file_path):
        for root, dirs, files in os.walk(file_path):
            dirs[:] = [] # 忽略子目录
            for f in files:
                move_file(os.path.join(root, f))
    elif  os.path.isfile(file_path):
        date_time  = time.strftime('%Y/%m',time.localtime(
                 os.path.getmtime(file_path)  # 文件最后修改时间
                 ))
        dirname = os.path.dirname(file_path)
        basename = os.path.basename(file_path)
        new_filepath = os.path.join(dirname, date_time, basename)
        os.renames(file_path, new_filepath)

def main():
    filepath = raw_input("please input the file or dir path:")
    move_file(filepath)

if __name__ == '__main__':
    main()
</pre>