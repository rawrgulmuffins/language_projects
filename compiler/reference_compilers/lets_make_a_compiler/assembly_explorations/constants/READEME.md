# What Is Being Tested?
This program is testing moving code into registers and memory.

So a program like

    1

should move the value 1 into the register

    %eax

and

    1 + 2

needs to move both the one and the two into two registers (eax and ebx).


# Resources
https://nickdesaulniers.github.io/blog/2014/04/18/lets-write-some-x86-64/

# Notes
## Different Registers from x86
[This shit took me way too segfaults to figure out.](http://zenit.senecac.on.ca/wiki/index.php/X86_64_Register_and_Instruction_Quick_Start)
## Minimum Viable Program
Don't know why yet but this is the boiler plate code that's required to not
have a segfault every time you run a program.
```
    .text
    .globl _main
    _main:
    subq $8, %rsp
    movq $0, %rdi
    call _exit
```
