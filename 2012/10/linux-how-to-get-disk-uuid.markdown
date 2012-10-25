# [Linux]如何获取磁盘分区的 UUID

有两种方法可以查看存储设备(/dev/sd\* /dev/hd\*)的 UUID 标识

# 使用 `blkid` 命令

    [redhat@localhost Desktop]$ sudo blkid
    /dev/sda1: UUID="71d84788-2d5f-4fc8-b43c-e4868763d9e8" TYPE="ext4" 
    /dev/sda2: UUID="df964274-abed-4e21-8bb1-0141f8756893" TYPE="ext4" 
    /dev/sda3: UUID="e5cdcd3f-186a-4967-bf4c-b00cb127443f" TYPE="ext4" 
    /dev/sda5: UUID="e99a6c9a-8ac4-473d-b450-d6de84d33473" TYPE="swap" 
    /dev/sda6: UUID="19356397-8d78-4671-a57c-7528b1d90a63" TYPE="ext4" 
    /dev/sda7: UUID="b8535d73-9fba-43d4-880f-45752bd66573" TYPE="ext4" 
    /dev/sda8: UUID="f5daae67-47f8-43de-bb59-b2ea6c7320dd" TYPE="ext4" 
    /dev/sda9: UUID="c78c8fee-8249-46e5-8a37-632e43f04e49" TYPE="swap" 
    /dev/sda10: UUID="244E1D284E1CF3F0" TYPE="ntfs" 
    /dev/sda11: UUID="0002284300013E2A" TYPE="ntfs" 
    [redhat@localhost Desktop]$ 


# 使用 `ls -l /dev/disk/by-uuid/` 命令

    [redhat@localhost Desktop]$ ls -l /dev/disk/by-uuid/
    total 0
    lrwxrwxrwx. 1 root root 11 Oct 25 12:26 0002284300013E2A -> ../../sda11
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 19356397-8d78-4671-a57c-7528b1d90a63 -> ../../sda6
    lrwxrwxrwx. 1 root root 11 Oct 25 12:26 244E1D284E1CF3F0 -> ../../sda10
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 71d84788-2d5f-4fc8-b43c-e4868763d9e8 -> ../../sda1
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 b8535d73-9fba-43d4-880f-45752bd66573 -> ../../sda7
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 c78c8fee-8249-46e5-8a37-632e43f04e49 -> ../../sda9
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 df964274-abed-4e21-8bb1-0141f8756893 -> ../../sda2
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 e5cdcd3f-186a-4967-bf4c-b00cb127443f -> ../../sda3
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 e99a6c9a-8ac4-473d-b450-d6de84d33473 -> ../../sda5
    lrwxrwxrwx. 1 root root 10 Oct 25 12:26 f5daae67-47f8-43de-bb59-b2ea6c7320dd -> ../../sda8
    [redhat@localhost Desktop]$ 

## 参考

 * [UsingUUID - Community Ubuntu Documentation](https://help.ubuntu.com/community/UsingUUID "UsingUUID - Community Ubuntu Documentation")
