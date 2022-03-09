# Barebones 6502 in Python

A learning experiment to see if I'm dumb enough to not understand how a CPU works.

[6502 reference](https://cx16.dk/6502/architecture.html)

## Initial thoughts (before watching the tutorial)

- The implementation is simple, so it can't be that hard
- The 6502 addresses 64KB of main memory over a 16-bit address bus, so we should initialize memory first (65536 or just FFFF)
- Addresses should be stored LSB first in memory
- 0000 to 00FF is called "zero-page" and does something interesting (special addressing modes)
- The last 6 bytes are also reserved and they HAVE to be programmed with the non-maskable interrupt handler at FFFA/B, the power on reset location at FFFC/D and the BRK/interrupt request handler at FFFE/F.
