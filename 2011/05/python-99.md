Python 输出 9x9 乘法表
python-99 
Python,9x9 乘法表

输出 9x9 乘法表：

<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: utf-8 -*-

for x in range(1, 10):
    a = []
    for y in range(1, x+1):
        a.append('%s x %s = %-2s  ' %(y, x, x*y))
    print ''.join(a)
</pre>

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    for x in range(1, 10):
        for y in range(1, x + 1):
            print '%s * %s = %-2s' % (y, x, y * x),
        print ''

输出结果：
<pre class="prettyprint">
1 x 1 = 1
1 x 2 = 2   2 x 2 = 4
1 x 3 = 3   2 x 3 = 6   3 x 3 = 9
1 x 4 = 4   2 x 4 = 8   3 x 4 = 12  4 x 4 = 16
1 x 5 = 5   2 x 5 = 10  3 x 5 = 15  4 x 5 = 20  5 x 5 = 25
1 x 6 = 6   2 x 6 = 12  3 x 6 = 18  4 x 6 = 24  5 x 6 = 30  6 x 6 = 36
1 x 7 = 7   2 x 7 = 14  3 x 7 = 21  4 x 7 = 28  5 x 7 = 35  6 x 7 = 42  7 x 7 = 49
1 x 8 = 8   2 x 8 = 16  3 x 8 = 24  4 x 8 = 32  5 x 8 = 40  6 x 8 = 48  7 x 8 = 56  8 x 8 = 64
1 x 9 = 9   2 x 9 = 18  3 x 9 = 27  4 x 9 = 36  5 x 9 = 45  6 x 9 = 54  7 x 9 = 63  8 x 9 = 72  9 x 9 = 81
</pre>
