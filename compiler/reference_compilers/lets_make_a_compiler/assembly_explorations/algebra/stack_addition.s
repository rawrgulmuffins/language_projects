.text
.globl _main
_main:
    subq $8, %rsp
    movq $1, %rax
    movq %rax, %rbx
    movq $2, %rax
    add %rax, %rbx
    movq $0, %rdi
    call _exit
