.text
.globl _main
_main:
  subq $8, %rsp
  movq $0, %rax
  movq %rax, %rbx
  movq $0, %rdi
  call _exit
