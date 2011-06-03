python 给文件名添加修改时间

python-rename-file-by-add-date-modified
python,


<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import re

"""添加文件修改日期到文件名
更新后的文件名类似：'test_2011_05_26_18_01.txt'
"""

# TODO:
# 1. 输入文件路径，重命名文件 √
# 2. 输入目录，批量重命名目录下的文件 √
# 3. 输入目录，遍历目录及子目录并重命名目录下的文件 √
# 4. 替换旧的时间 √

# os.path.getmtime(path) 
# os.path.basename(path)
# os.path.realpath(path)
# os.path.dirname(path) 
# os.rename(src, dst) 
# os.path.isdir(path) 
# os.path.isfile(path) 
# os.listdir(path)

# 遍历目录
def file_paths(dir_path):
    list_dirs = os.listdir(dir_path) # 获取给定目录下的文件及文件夹
    for dir in list_dirs:
        dir = os.path.realpath(dir_path + '/' + dir)
        print dir
        if os.path.isfile(dir):
            update_filename(dir)
        # if os.path.isdir(dir): # 如果是文件夹
            # file_paths(dir)  # 遍历子目录

def rename_file(file_path, old_filename, new_filename):
    os.rename(os.path.realpath(file_path), 
                        os.path.realpath(
                        os.path.dirname(file_path) # 文件所在目录的路径
                        +'/' + new_filename)
                    ) 
    # print '文件名更新成功！'
    # print 原文件名  更新后的文件名

def update_filename(file_path):
    """添加文件修改日期到文件名
    更新后的文件名类似：'test_2011_05_26_18_01.txt'
    用法： update_filename(文件路径)
    无返回值
    """
    date_modified = time.strftime('_%Y_%m_%d_%H_%M',
                                time.localtime(
                                os.path.getmtime(file_path)  # 文件最后修改时间
                                )) # 格式化日期
     
    file_basename = os.path.basename(file_path)
    # 移除旧的日期
    file_basename = re.sub(r'(_\d{4}_\d{2}_\d{2}_\d{2}_\d{2})+$', '',
                                                file_basename)
    m = re.match(r'(.*?)(\.\w+)$', 
                                # 返回路径中的文件名 类似 'test.txt'
                                file_basename
                                ) # 查找文件名及扩展名
    # 分离文件名及扩展名
    try:
        old_filename = [m.group(1), m.group(2)] # 类似：['updatefilename', '.py']
    except:
        old_filename = [file_basename, '']  # 文件无扩展名
    
    # print old_filename
    # a.insert(1,'c')
    new_filename = old_filename[0] + date_modified + old_filename[1]
    # print new_filename
    # 重命名操作
    rename_file(file_path, old_filename, new_filename)
    
def main():
    filepath = raw_input('Please input the filepath: ')
    update_filename(filepath)
    # TODO:
    # 判断输入的路径是文件还是文件夹  √
    # if os.path.isfile(filepath):
    #   update_filename(filepath)
    # if os.path.isdir(filepath):
    #   file_paths(filepath)
    #print filepath
    
if __name__ == '__main__':
    main()

</pre>

