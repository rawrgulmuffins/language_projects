.text
.globl _main
_main:
    subq $8, %rsp
    movq $2, %rax
    push %rax
    movq $1, %rax
    pop %rbx
    sub %rax, %rbx
    movq $0, %rdi
    call _exit
