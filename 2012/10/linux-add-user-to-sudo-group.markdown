# [linux] Red Hat 中如何给用户添加 sudo 命令的使用权限

修改 `/etc/sudoers` 文件即可。

比如要给予 test 用户 sudo 命令的使用权限，进行如下操作即可。

    [test@localhost home]$ sudo ls /root
    [sudo] password for test:
    test is not in the sudoers file.  This incident will be reported.
进入 root 用户修改 `/etc/sudoers` 文件

    [test@localhost home]$ su
    Password:
    [root@localhost home]# vim /etc/sudoers
找到 root 相关项： `root    ALL=(ALL)      ALL`，仿照它添加 test 用户,
最终文件中应当包含：

    root    ALL=(ALL)      ALL
    test    ALL=(ALL)      ALL
测试

    [root@localhost home]# vim /etc/sudoers
    [root@localhost home]$ exit
    exit
    [test@localhost home]$ sudo ls /root
    [sudo] password for test:
    anaconda-ks.cfg  install.log  install.log.syslog

## 参考

 * [4.4.3.2. The sudo Command - Red Hat Customer Portal](https://access.redhat.com/knowledge/docs/en-US/Red_Hat_Enterprise_Linux/4/html/Security_Guide/s3-wstation-privileges-limitroot-sudo.html "4.4.3.2. The sudo Command - Red Hat Customer Portal")
