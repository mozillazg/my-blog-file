匹配除两个特定子域名外的其他子域名

假设这两个特定子域名是：abc.test.com、adc.test.com

正则表达式如下：

        \w+(?<!abc|adc)\.test\.com
测试结果(蓝色为匹配内容):       
abc.test.com    
adc.test.com    
<strong style="color:blue">aaa.test.com</strong>    
<strong style="color:blue">aabca.test.com</strong>      

请多指教

