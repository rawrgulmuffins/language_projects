.text
.globl _main
_main:
    subq $8, %rsp
    movq $1, %rax
    push %rax
    movq $2, %rax
    pop %rbx
    add %rax, %rbx
    movq $0, %rdi
    call _exit
