# [python]第三方模块管理工具：pip

pip 是个 python 第三方模块管理工具，类似 [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall)。

>pip is a tool for installing and managing Python packages, such as those found in the [Python Package Index](http://pypi.python.org/pypi "link-to-pypi"). It’s a replacement for [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall).

我的直观感受（Windows 下）就是它比 easy\_install 方便：`easy_install` 需要管理员权限才能执行，每次使用都需要去开个管理员权限的命令行，而 `pip` 可以在普通命令行下执行

## 安装

安装 pip 之前，需要先安装 [setuptools](http://pypi.python.org/pypi/setuptools "link-to-setuptools") 或 [distribute](http://pypi.python.org/pypi/distribute "link-to-distribute")。

安装 pip

* 使用 `easy_install` 进行安装（不推荐，刚才试了一下发现使用此方法安装的 pip 版本比较老）：

    easy_install pip

* 使用源码安装（推荐）：

    1. 从 [http://pypi.python.org/pypi/pip/](http://pypi.python.org/pypi/pip/ "link-to-pip-src") 下载 pip 的源代码
    2. 解压源代码，进入源代码内 setup.py 所在目录，执行：

            python setup.py install

## 使用

安装第三方模块：

    $ pip install simplejson
    [... progress report ...]
    Successfully installed simplejson

升级某个模块：

    $ pip install --upgrade simplejson
    [... progress report ...]
    Successfully installed simplejson

移除某个模块：

    $ pip uninstall simplejson
    Uninstalling simplejson:
      /home/me/env/lib/python2.7/site-packages/simplejson
      /home/me/env/lib/python2.7/site-packages/simplejson-2.2.1-py2.7.egg-info
    Proceed (y/n)? y
      Successfully uninstalled simplejson

## 参考

 * [pip 帮助文档](http://www.pip-installer.org/en/latest/ "pip doc")
