#[vim]禁用 Scratch 窗口

Scratch 窗口主要用于在切换代码补全信息时显示文档字符串。
但是大多数时候提供的信息没什么用，这就有点碍事了。

![scratch-window](https://github.com/mozillazg/my-blog-file/raw/master/2012/11/vim-scratch-window.png "scratch-window")

下面说一下如何禁用 Scratch 窗口。

在配置文件（.vimrc/\_vimrc）中修改或增加 `completeopt` 选项：

    set completeopt=menu
或：

    set completeopt-=preview

原则就是 `completeopt` 的值不能包含 `preview`，
具体请看帮助： `:help completeopt`


