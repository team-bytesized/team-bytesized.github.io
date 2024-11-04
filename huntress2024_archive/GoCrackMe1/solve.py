from pwn import *
context.binary = './GoCrackMe1'
elf = process('./GoCrackMe1')

pid, iodbg = gdb.attach(elf, gdbscript='''
b main.main
run
b main.checkCondition
continue
x /s $rax
''', api=True)

elf.recvline()