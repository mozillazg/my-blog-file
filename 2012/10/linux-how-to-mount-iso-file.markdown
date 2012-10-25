# [Linux] 如何挂载 iso 文件

linux 系统中使用 `mount` 命令即可挂载 iso 文件

    [redhat@localhost home]$ ls /media
    [redhat@localhost home]$ sudo mount -o loop ubuntu.iso /media
    [redhat@localhost home]$ ls /media
    autorun.inf  dists     md5sum.txt  preseed             wubi.exe
    boot         install   pics        README.diskdefines
    casper       isolinux  pool        ubuntu
    [redhat@localhost home]$ 

使用 `umount` 卸载

    [redhat@localhost home]$ ls /media
    autorun.inf  dists     md5sum.txt  preseed             wubi.exe
    boot         install   pics        README.diskdefines
    casper       isolinux  pool        ubuntu
    [redhat@localhost home]$ sudo umount /media
    [redhat@localhost home]$ ls /media
    [redhat@localhost home]$ 

