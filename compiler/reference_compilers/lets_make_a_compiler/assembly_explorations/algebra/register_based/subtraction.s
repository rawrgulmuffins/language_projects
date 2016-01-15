.text
.globl _main
_main:
    subq $8, %rsp
    movq $2, %rax
    movq %rax, %rbx
    movq $1, %rax
    sub %rax, %rbx
    movq $0, %rdi
    call _exit
