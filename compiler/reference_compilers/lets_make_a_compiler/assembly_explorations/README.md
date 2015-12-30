# What Is This?
This directory contains all of the assembly programs that were produced in
order to write the unit tests for the compiler found one directory above.

# Why Is This Here?
I found myself writing `x86_64` assembly code that might or might not be valid
and I need to find out if the code did what I actually expected it to do. So
all of these are the discovery steps to test correctness.

# How Can I Use These?
Each directory contains a simple assembly program and a make file. Simple
traverse to the code sample you want to use and run

    make
    make clean

then

   ./program_name

# Structure

Each directory contains 

A simple reference explaining what's the point of this program and notes about
things learned.

    README.md 

A make file for assembling and linking

    makefile

The program itself

    something.s # Reference to using as as the assembler
