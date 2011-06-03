<span style="color:red; font-weight: blod;">本文转自：</span><http://qingbo.net/picky/502-markdown-syntax.html> | 作者：qingbo



Markdown 的语法的权威介绍是 Daring Fireball 的 [Markdown Syntax Documentation](http://daringfireball.net/projects/markdown/syntax)，不过有一些 Markdown 的实现对原本的 Markdown 语法作了扩展。本页面仅作为简单的参考，并不是对这个文档的翻译，因此懂英文的都应该去读 Markdown Syntax Documentation.


##最常用格式


    * 空一行（两个回车）分段
    * 行末加两个或多个空格才是真正的换行，否则正常的一个回车就像在 HTML 代码中一样，被当作空格处理
    * 插入链接： [链接文字](url)
    * 图片跟链接很像，在前面加个叹号：![alt 文字](图片 URL)


段落和换行有什么区别？段落在生成的 HTML 代码中被一对 `<p></p>` 标签包含起来，而换行只是插入了一个 `<br />` 标签。一般来说，网页设计给段落之间留的空白应该比行距大。


##其它格式


下面会遇到一些语法需要在许多行前插入统一的缩进或特殊符号的，因此你需要一个非常舒服的[支持列编辑模式的文本编辑器][editor]。

  [editor]: http://qingbo.net/picky/509-column-editing.html


###内嵌 HTML


由于内嵌 HTML 可以做 HTML 能做的任何事情，因此在用户可以自由输入的地方，需要禁用此功能，比如本站点的评论框。


    * block level elements 像 p, div 之类的，需要前后各空一行（两个回车），并且开始和结束标签那一行的前面不能用空格或 Tab 缩进。
    * span level elements 如 a, img 可以在任何地方使用


###标题


用 1-6 个井号 (#) 开始一行表示这一行是标题，例如：


    # 一级标题
    ## 二级标题
    ###### 六级标题


###blockquote


用右尖括号 `(>)` 表示 blockquote，你一定见过邮件中这样表示引用别人的内容。可以嵌套，可以包含其它的 Markdown 元素，例如：

    > ## This is a header.
    >
    > 1.   This is the first list item.
    > 2.   This is the second list item.
    >
    > Here's some example code:
    >
    >     return shell_exec("echo $input | $markdown_script");

###列表

HTML 列表分无序列表 (unordered list, ul) 和有序列表 (ordered list, ol) 两种。在 Markdown 中用星号、加号、减号开始一行表示无序列表，用数字开始一行表示有序列表。例如：

    *   Red
    *   Green
    *   Blue
    
    1.  Bird
    2.  McHale
    3.  Parish

当然在有序列表中不必完全按照数字顺序标记，不过最好第一个条目使用数字 1. 列表的标记符号一般写在一行的开始，不过也可以在前面加最多三个空格 (如果加四个空格就表示是源代码了，见后文)。

###代码及代码块

如果是在一段文字中插入一句代码，把代码用 (`) 符号包围起来即可。这个符号在键盘左上角，1 的左边，Tab 的上面。

如果插入一大段代码也很简单，在代码的每一行之前加四个空格。

###横线

三个或以上星号、减号或者下划线单独放在一行即可生成一条横线 (horizontal rule, hr). 以下例子都是可以的：

    * * *
    ***
    *****
    - - -
    ---------------------------------------

###强调

用星号或下划线来实现。两边分别放一个 * 或 _ 会生成 em 标签，放两个则生成 strong 标签。例如：

    *单星号*
    
    _单下划线_
    
    **双星号**
    
    __双下划线__
    
会生成:
    
    <em>单星号</em>
    
    <em>单下划线</em>
    
    <strong>双星号</strong>
    
    <strong>双下划线</strong>


<span style="color:red; font-weight: blod;">PS.</span>  
  * 本文的 Markdown 格式源文件下载：[markdown-syntax.md](http://cid-af460b95f4270da2.office.live.com/self.aspx/.Public/markdown-syntax.md)

