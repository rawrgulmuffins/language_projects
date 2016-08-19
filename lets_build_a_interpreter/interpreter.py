"""This program is an interpreter for a subset of the PASCAL programming
language. It's' based off of the Let's Build A Simple Interpreter tutorial
found at https://ruslanspivak.com/lsbasi-part1/

This code base was build and tested in Python3.5.
"""
INTEGER, EOF, PLUS = 'INTEGER', 'PLUS', 'EOF'

class Token:

    def __init__(self, type, value):
        """Simple creation method used to build Tokens.

        NOTE: no verification of data is currently being done. Later versions
        of this class should check for invalid values based on passed in type
        and invalide types.
        """
        self.type = type
        self.value = value

    def __str__(self):
        """Produces a human readable representation of this objects meta data
        and data.
        """
        pass

    def __repr__(self):
        """Produces a string that, if passed to a python interpreter with the
        Token type defined, will create a new Token object with the current
        variables.
        """
        pass
