忘记 Ubuntu 10.10 登录密码时，通过 recovery mode 修改用户密码

我只在 VirtualBox 虚拟机中安装了 Ubuntu，所以图片是虚拟机中的，不过可以作为参考。      
当忘记 Ubuntu 用户名密码时，可以通过进入 <span style="font-weight: blod;">recovery mode</span> 修改用户密码。  

在 VirtualBox 中步骤如下：

1.   开机按 F12 进入 boot 设置      
![boot][link0]
2.  按 b     
![b][link1]
3.   选择 "recovery mode" 回车      
![recovery mode][link2]
4.   选择 "root shell" 回车     
![root shell][link3]    
![root shell][link4]
5.   输入"ls /home"查看用户名      
![ls /home][link5]
6.   输入"passwd username"这里的username就是您的用户名 ，修改密码        
![passwd username][link6]
7.   输入两次密码     
![passwd][link7]
8.   重启

  [link0]: http://mzgphotos.appspot.com/showimage/34001/
  [link1]: http://mzgphotos.appspot.com/showimage/41001/
  [link2]: http://mzgphotos.appspot.com/showimage/40001/
  [link3]: http://mzgphotos.appspot.com/showimage/39001/
  [link4]: http://mzgphotos.appspot.com/showimage/38001/
  [link5]: http://mzgphotos.appspot.com/showimage/37001/
  [link6]: http://mzgphotos.appspot.com/showimage/36001/
  [link7]: http://mzgphotos.appspot.com/showimage/35001/ 

