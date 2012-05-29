# [python]使用 PAMIE 控制 IE 浏览器

> PAMIE是一套为Python写的用于Web自动化测试的工具，采用Win32COM的方式操作IE来实现。

可以用 PAMIE 来进行自动提交表单、自动点击之类的工作。

## 安装及配置

从 [http://sourceforge.net/projects/pamie/files/](http://sourceforge.net/projects/pamie/files/) 下载适合自己 Python 版本的 PAMIE 压缩包。本文下载的是 pamie20.zip 适用于 Python 2.x 。

将压缩包内的 cPAMIE.py 拷贝到 python/lib 目录下。网上有说 <cite>注意 sys.path.append后面的路径是否正确，如果不正确需要修改一下，修改为python模块的路径即可，比如 sys.path.append(r'd:\python26\lib')</cite> ，经验证可以不用修改 cPAMIE.py 的内容。

在压缩包内的 readme.html 中可以找到一个 api 文档(PAMIE Reference Guide)。

还有就是需要下载相应版本的 Python Win32 扩展：<http://sourceforge.net/projects/pywin32/files/>

## 使用

至于使用方法，可以查看 api 文档或上网搜索。

下面主要讲述一下我在使用中遇到的几个问题。

### 系统环境

 * Windows 7 Ultimate 32-bit
 * Python 2.6.7 + cPAMIE Build 2.0
 * Internet Explorer 8

### 遇到的问题

遇到的第一个问题是：

    >>> from cPAMIE import PAMIE
    >>>
    >>> ie = PAMIE()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "e:\Program Files\Python\lib\cPAMIE.py", line 64, in __init__
        self._ie = DispatchEx('InternetExplorer.Application')
      File "e:\Program Files\Python\lib\site-packages\win32com\client\__init__.py", line 113, in DispatchEx
        dispatch = pythoncom.CoCreateInstanceEx(clsid, None, clsctx, serverInfo, (pythoncom.IID_IDispatc
    h,))[0]
    pywintypes.com_error: (-2147221005, 'Invalid class string', None, None)
    
上网查了 n 久以后才知道可能跟注册表中的 `HKEY_CLASSES_ROOT\InternetExplorer.Application` 的值有关。

所以我就对注册表中相关项做了如下修改：

    Windows Registry Editor Version 5.00
    
    [HKEY_CLASSES_ROOT\InternetExplorer.Application]
    @="Internet Explorer"
    
    [HKEY_CLASSES_ROOT\InternetExplorer.Application\CLSID]
    @="{0002DF01-0000-0000-C000-000000000046}"
    
    [HKEY_CLASSES_ROOT\InternetExplorer.Application\CurVer]
    @="InternetExplorer.Application.1"



    Windows Registry Editor Version 5.00
    
    [HKEY_CLASSES_ROOT\InternetExplorer.Application.1]
    @="Internet Explorer (Ver 1.0)"
    
    [HKEY_CLASSES_ROOT\InternetExplorer.Application.1\CLSID]
    @="{0002DF01-0000-0000-C000-000000000046}"

这样做了以后又出现了另外一个问题：

    >>> ie = PAMIE()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "E:\Program Files\Python\lib\cPAMIE.py", line 64, in __init__
        self._ie = DispatchEx('InternetExplorer.Application')
      File "E:\Program Files\Python\lib\site-packages\win32com\client\__init__.py", line 113, in DispatchEx
        dispatch = pythoncom.CoCreateInstanceEx(clsid, None, clsctx, serverInfo, (pythoncom.IID_IDispatch,))[0]
    pywintypes.com_error: (-2147221164, 'Class not registered', None, None)
    
经实验，只要在先打开 IE 浏览器后再执行上面的代码就不会出错了。

### 关于 javaScriptExecute() 函数

还有就是我发现它的 api 文档中关于 javaScriptExecute() 函数的描述有误：

> javaScriptExecute() Function      
> Executes a java script function
> 
>   Parameters:     
>   javaScriptExecute (name)        
> 
>   name: The name of the javascript function       
> 
>   Returns:        
>   True on success, else False

实际情况是 javaScriptExecute() 函数根本就没有返回值。需要修改源代码中的 javaScriptExecute() 函数，为其添加返回值：

    
    def javaScriptExecute(self, name):
        """ Executes a java script function
            parameters:
                name  - The name of the javascript function
            returns:
                True on success, else False
        """
        self._wait() 
        try:
            doc = self._ie.Document
            pw = doc.parentWindow
            script = name
            pw.execScript(script)
            return True
        except: 
            (ErrorType,ErrorValue,ErrorTB)=sys.exc_info()
            print sys.exc_info()
            traceback.print_exc(ErrorTB)
            return False
    

## 参考

 * [Python开发的IE自动化程序工具pamie安装配置](http://iamcaihuafeng.blog.sohu.com/156855572.html)
 * [转：PAMIE- Python实现IE自动化的模块](http://www.cnblogs.com/babykick/archive/2011/06/10/2077330.html)
 * [[求助] CreateObject("InternetExplorer.Application")问题](http://social.technet.microsoft.com/Forums/zh-CN/windowsxpzhchs/thread/98206d70-dfb3-4349-85d9-06983fedf63e)


PAMIE,cPAMIE,InternetExplorer,InternetExplorer.Application,IE8,InternetExplorer.Application does not work for IE8,Invalid class string,pywin32,

