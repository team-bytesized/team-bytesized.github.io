from pwn import *

movelist = [b'retreat', b'advance', b'strike', b'block']

map = {
    b'retreat': b'strike\n',
    b'advance': b'retreat\n',
    b'strike': b'block\n',
    b'block': b'advance\n'
}

conn = remote('challenge.ctf.games', 31592)

while True:
    try:
        m1 = conn.recv()
    except EOFError:
        break
    # Decode the received bytes into a UTF-8 string
    decoded_message = m1.decode('utf-8', errors='ignore')  # Ignoring any invalid characters
    if 'flag' in decoded_message:
        print(decoded_message)
    for move in movelist:
        if move in m1:
            # Send the corresponding move (already in bytes)
            conn.send(map[move])
            break