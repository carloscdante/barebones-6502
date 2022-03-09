# Barebones 6502 in Python

![6502](https://hackerspace.ie/wp-content/uploads/2020/06/s-l1600-2.jpg)

A learning experiment to see if I'm dumb enough to not understand how a CPU works.

[6502 reference](https://cx16.dk/6502/architecture.html)

## Initial thoughts (before watching the tutorial)

- The implementation is simple, so it can't be that hard
- The 6502 addresses 64KB of main memory over a 16-bit address bus, so we should initialize memory first (65536 or just FFFF)
- Addresses should be stored LSB first in memory
- 0000 to 00FF is called "zero-page" and does something interesting (special addressing modes)
- 0100 to 01FF is the stack (256 bytes of stack)
- The last 6 bytes are also reserved and they HAVE to be programmed with the non-maskable interrupt handler at FFFA/B, the power on reset location at FFFC/D and the BRK/interrupt request handler at FFFE/F.
- We have to emulate the registers.

## The Program Counter

The program counter is the pointer to the address that the CPU is executing the code for. Whatever address is in there will be the next instruction to be executed.
