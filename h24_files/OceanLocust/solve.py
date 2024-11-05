import struct


def parse(data):
    decoded_data = b""
    for letter in range(ord("a"), ord("h") + 1):  # biTa to biTh
        chunk_name = f"biT{chr(letter)}".encode()
        if chunk_name in data:
            start_index = data.index(chunk_name) + len(chunk_name)
            additional_data = data[start_index : start_index + 6]
            unpacked_data = struct.unpack("6B", additional_data)
            decoded_data += bytes(
                a ^ b for a, b in zip(unpacked_data[:5], [*chunk_name, chunk_name[0]])
            )
    print(decoded_data.strip(b"\xaa").decode())


parse(open("inconspicuous.png", "rb").read())
