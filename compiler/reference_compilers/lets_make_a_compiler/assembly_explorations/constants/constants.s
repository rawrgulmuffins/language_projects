.text
.globl _main
_main:
    mov $1, %eax
    mov %eax, %ebx
    mov $2, %eax
    call _exit
