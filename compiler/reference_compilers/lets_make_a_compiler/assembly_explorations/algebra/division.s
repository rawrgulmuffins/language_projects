.text
.globl _main
_main:
    subq $8, %rsp
    movq $2, %rax
    push %rax
    movq $1, %rax
    movq %rax, %rbx
    pop %rax
    # Took waaay to long to figure this out. Information at
    # https://stackoverflow.com/questions/8858104/64bit-nasm-division-idiv
    xor  %rdx, %rdx # clear high bits of dividend 
    div %rbx
    movq $0, %rdi
    call _exit
