# Reference Materials
[Compiler tutorial](http://compilers.iecc.com/crenshaw/)
[x86_64 writing to stdout](http://0xax.blogspot.com/2014/11/say-hello-to-x64-assembly-part-4.html)
[More string printing in x86_64](https://stackoverflow.com/questions/27594297/how-to-print-a-string-to-the-terminal-in-x86-64-assembly-nasm-without-syscall)


## X86_64 Referece Material
https://nickdesaulniers.github.io/blog/2014/04/18/lets-write-some-x86-64/
# Notes On Introduction
## FPC
* OSX needs the free pascal compiler which is almost equivilent to turbo pascal.
* http://www.toosquare.com/2014/07/install-pascal-on-os-x/
## Assembly language 
* 68000 code is the assembly language used.
* My Macbook uses X86_64
* TODO: Translate from 68000 to X86_64
* NOTE: Giving up on containing both 68000 code and X86. I'd need to get into
        full ABST or Bytecode in order to make it actually managable.

# EBNF Of The Languages

<expression> ::= <term> [<addop> <term>]*
<term> ::= <factor>  [ <mulop> <factor> ]*
<factor> ::= (<expression>)


