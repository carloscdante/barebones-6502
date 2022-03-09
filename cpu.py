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

opcodes = {
    0xA9: 'INS_LDA_IM',
}

# instruction fetch

def map_opcode(op):
    return opcodes.get(op)

def read(addr):
    return data[addr]

def fetch(cycle, memory):
    global PC
    global data
    return data[PC]

def init_memory(memory):
    for i in range(memory):
        data[i] = 0

def step(cycle, memory):
    global PC, SP, C, Z, I, D, B, V, N, A, X, Y
    while cycle > 0:
        next = fetch(cycle, memory)
        cycle -= 1
        PC += 1
        opcode = map_opcode(next)
        if(opcode == 'INS_LDA_IM'):
            val = fetch(cycle, memory)
            A = val
            if(A == 0): Z = 1
            if(A & 0b10000000) > 0: N = 1
        if(opcode == ''):
            print('No instruction provided')


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
    global A
    reset(memory)
    data[0xFFFC] = 0xA9
    data[0xFFFD] = 0x42
    step(2, memory)
    print(A)
    return 0

run()