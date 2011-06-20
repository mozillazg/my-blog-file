正则表达式中多选结构

        ...|...

相当于 `if ... elif ... else` 

###多选结构内的表达式的顺序不一样所匹配的结果也可能不一样

`1|100` 只能匹配1而匹配不了100(蓝色为匹配内容):      
<strong style="color:blue">1</strong>    
<strong style="color:blue">1</strong>00     

