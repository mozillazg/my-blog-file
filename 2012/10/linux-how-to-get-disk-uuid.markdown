# [Linux]如何获取磁盘分区的 UUID

有两种方法可以查看存储设备(/dev/sd\* /dev/hd\*)的 UUID 标识

# 使用 `blkid` 命令

    [redhat@localhost Desktop]$ sudo blkid
    /dev/sda1: UUID="71d84788-2d5f-4fc8-b43c-e4868763d9e8" TYPE="ext4" 
    /dev/sda2: UUID="df964274-abed-4e21-8bb1-0141f8756893" TYPE="ext4" 
    ...
    /dev/sda11: UUID="0002284300013E2A" TYPE="ntfs" 
    [redhat@localhost Desktop]$ 


# 使用 `ls -l /dev/disk/by-uuid/` 命令

    [redhat@localhost Desktop]$ ls -l /dev/disk/by-uuid/
    total 0
    lrwxrwxrwx. 1 root root 11 Oct 25 12:26 0002284300013E2A -> ../../sda11
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 19356397-8d78-4671-a57c-7528b1d90a63 -> ../../sda6
    ...
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 f5daae67-47f8-43de-bb59-b2ea6c7320dd -> ../../sda8
    [redhat@localhost Desktop]$ 

## 参考

 * [UsingUUID - Community Ubuntu Documentation](https://help.ubuntu.com/community/UsingUUID "UsingUUID - Community Ubuntu Documentation")
