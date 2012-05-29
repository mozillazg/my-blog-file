##web.py 分页

###代码

Python:

    def GET(self, page=1):
        page = int(page)
        perpage = 2
        offset = (page - 1) * perpage
        posts = db.select("entries", order="id DESC", offset=offset,
                                    limit=perpage)
        postcount = db.query("SELECT COUNT(*) AS count FROM entries")[0]
        pages = postcount.count / perpage
        if postcount.count % perpage > 0:
            pages += 1
        if page > pages:
            raise web.seeother('/')
        else:
            return render.index(posts=posts, pages=pages)

模板：

    $for page in range(1, pages + 1):
        <a href="/page/$page">$page</a>

###参考：

 * <http://www.mengu.net/post/pagination-with-webpy>
