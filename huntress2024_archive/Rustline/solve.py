a = open("challenge-files/password.txt","rb").read()
b = open("encrypted-files/password.txt","rb").read()
repeatedkey = bytes([i^j for i,j in zip(a,b)])
print(repeatedkey)

key = br"\xb8\xf7/\xf6\x95XwE\xb0\x8f"
extended_key=key*1000
ct= open("encrypted-files/flag.txt","rb").read()
pt=bytes([i^j for i,j in zip(ct,extended_key)])
print(pt)