
最近试用了一下 pylint.vim，结果 `:Pylint` 命令显示如下结果：

![before](https://github.com/mozillazg/my-blog-file/raw/master/2011/11/2011-11-05-09-36-5.jpg)

基本上没什么用，因此做了如下更改：

![change](https://github.com/mozillazg/my-blog-file/raw/master/2011/11/2011-11-05-09-38-4.jpg)

将 69 行附近的

    "CompilerSet makeprg=(echo\ '[%]';\ pylint\ -r\ y\ %)
改为：

    CompilerSet makeprg=pylint\ --reports=n\ --output-format=parseable\ %:p
75行附近的

    "CompilerSet efm=%+P[%f],%t:\ %#%l:%m,%Z,%+IYour\ code%m,%Z,%-G%.%#
改为：

    CompilerSet efm=%A%f:%l:\ [%t%.%#]\ %m,%Z%p^^,%-C%.%#

更改后 `:Plint` 命令结果如下：

![after](https://github.com/mozillazg/my-blog-file/raw/master/2011/11/2011-11-05-09-37-2.jpg)

##参考

* [Integrate Pylint and Pychecker support](http://vim.wikia.com/wiki/Integrate_Pylint_and_Pychecker_support)

