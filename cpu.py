import struct

regfile = [0]*0xFFFC

# 64k
memory = 0xFFFF
data = range(memory)

# Program counter
PC = 128

# Stack pointer
SP = 64

# Registers
A = 64
X = 64
Y = 64

C = 1
Z = 1
I = 1
D = 1
B = 1
V = 1
N = 1

# instruction fetch

def read(addr):
    return data[addr]

def fetch(cycle, memory):
    global PC
    global data
    PC += 1
    return data[PC]

def init_memory(memory):
    for i in range(memory):
        data[i] = 0

def step(cycle, memory):
    while cycle > 0:
        cycle -= 1
        next = fetch(cycle, memory)

def reset(memory):
    # reset process
    global PC, SP, C, Z, I, D, B, V, N, A, X, Y
    PC = 0xFFFC
    SP = 0x0100
    C = 0
    Z = 0
    I = 0
    D = 0
    B = 0
    V = 0
    N = 0
    A = 0
    X = 0
    Y = 0
    init_memory(memory)

def run():
    reset(memory)
    step(2, memory)
    return 0

run()