#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import socket
import time

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 5200))
    s.listen(5)
    print 'server running'

    conn, addr = s.accept()
    while True:
        conn, addr = s.accept()
        upload_content = conn.recv(20240)
        print 'from %s, file length: %s' % (addr, len(upload_content))

        name = 'from_client/' + str(time.time())
        with open(name, 'w') as f:
            f.write(str(upload_content))

        conn.send('ok')
        print 'file has been saved: "%s"' % name
        conn.close()
