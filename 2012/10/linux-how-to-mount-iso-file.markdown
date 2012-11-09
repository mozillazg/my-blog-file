# [Linux] 如何挂载 iso 文件

linux 系统中使用 `mount -o loop` 命令即可挂载 iso 文件

    [redhat@localhost home]$ ls /media
    [redhat@localhost home]$ sudo mount -o loop ubuntu.iso /media
    [redhat@localhost home]$ ls /media
    autorun.inf  dists     md5sum.txt  preseed             wubi.exe
    [redhat@localhost home]$ 
如果不行的话，再试试 `mount -t iso9660 -o loop test.iso /media`

使用 `umount` 卸载

    [redhat@localhost home]$ ls /media
    autorun.inf  dists     md5sum.txt  preseed             wubi.exe
    [redhat@localhost home]$ sudo umount /media
    [redhat@localhost home]$ ls /media
    [redhat@localhost home]$ 

顺便说一下制作 iso 光盘镜像文件的方法：

    cp /dev/cdrom test.iso
