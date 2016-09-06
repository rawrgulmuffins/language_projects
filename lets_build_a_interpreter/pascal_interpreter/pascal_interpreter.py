"""This program is an interpreter for a subset of the PASCAL programming
language. It's' based off of the Let's Build A Simple Interpreter tutorial
found at https://ruslanspivak.com/lsbasi-part1/

This code base was build and tested in Python3.5.
"""
INTEGER, EOF, PLUS = 'INTEGER', 'PLUS', 'EOF'

class InterpreterError(Exception):
    """Default exception for the interpter. Only thrown as a last resort. 
    Normally this means a more strict exception wasn't found. If you see this
    kind of exception in the wild consider putting in an enchancement request
    for a more narrow exception type for the given erroneous input.
    """
    pass

class Token:

    def __init__(self, type, value):
        """Simple creation method used to build Tokens.

        args:
            type: A name used to associate what kind and parameters of data
                that will be present in the Token object.
            value: A value that's hopefully valid for the passed in data type.
                example is that INTEGER type is associated with 
                -1, 0, 1, 2, ...

        NOTE: no verification of data is currently being done. Later versions
        of this class should check for invalid values based on passed in type
        and invalide types.
        """
        self.type = type
        self.value = value

    def __str__(self):
        """Produces a human readable representation of this objects meta data
        and data.

        For now this is simple enough that we're just returning the machine
        readable format. Subject to change as complexity increases.
        """
        return self.__repr__()

    def __repr__(self):
        """Produces a string that, if passed to a python interpreter with the
        Token type defined, will create a new Token object with the current
        variables.
        """
        return "Token(type={type}, value={value})".format(
                type=self.type,
                value=self.value,
            )

class Interpreter:

    def __init__(self, text):
        """
        """
        # Text to be interpreted
        # NOTE: no verification at this point in time.
        self.text = text
        # position of the index on self.text
        self.pos = 0
        # current token
        self.current_token = None

    def _error(self):
        """
        """
        # NOTE: force students to test these kinds of functions so they catch
        # things like mis-namings.
        raise InterpreterError()

    def _next_token(self):
        """
        """
        pass

    def _consume_token(self, token_type):
        """
        """
        pass

    def _parse(self):
        """
        """
        pass
