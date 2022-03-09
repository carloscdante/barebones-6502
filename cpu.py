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
    0xA5: 'INS_LDA_ZP',
    0xB5: 'INS_LDA_ZPX',
    0x20: 'INS_JSR'
}

# instruction fetch

def map_opcode(op):
    return opcodes.get(op)

def read(cycle, addr):
    return data[addr]

def fetch(cycle, memory):
    global PC
    global data
    return data[PC]

def fetch_word(cycle, memory):
    global PC
    global data
    unit = data[PC]
    unit |= (data[PC] << 8)
    return data[PC]

def write_word(value, addr):
    data[addr] = value & 0xFF
    data[addr + 1] = (value >> 8)

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
        if(opcode == 'INS_LDA_ZP'):
            zpa = fetch(cycle, memory)
            A = read(cycle, zpa)
            PC -= 1
        if(opcode == 'INS_LDA_ZPX'):
            zpa = fetch(cycle, memory)
            zpa += X
            A = read(cycle, zpa)
            PC -= 1
        if(opcode == 'INS_JSR'):
            subaddr = fetch_word(cycle, memory)
            cycle -= 2
            data[SP] = PC - 1
            write_word(PC - 1, SP)
            PC = subaddr
            SP += 1
            cycle -= 1

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
    data[0xFFFC] = 0x20
    data[0xFFFD] = 0x42
    data[0xFFFE] = 0x42
    data[0x0042] = 0xA9
    data[0x0043] = 0x84
    step(6, memory)
    print(A)
    return 0

run()