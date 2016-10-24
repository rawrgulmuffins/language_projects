"""This program is an interpreter for a subset of the PASCAL programming
language. It's' based off of the Let's Build A Simple Interpreter tutorial
found at https://ruslanspivak.com/lsbasi-part1/

This code base was build and tested in Python3.5.
"""
# NOTE: So when I made this I made the mistake of switching the token strings.
# My "test_eof_at_end_of_line" test found the error.
INTEGER, EOF = "INTEGER", "EOF"
PLUS, MINUS, TIMES, DIVIDED_BY = ("PLUS", "MINUS", "TIMES", "DIVIDED_BY")

class InterpreterError(Exception):
    """Default exception for the interpter. Only thrown as a last resort.
    Normally this means a more strict exception wasn't found. If you see this
    kind of exception in the wild consider putting in an enchancement request
    for a more narrow exception type for the given erroneous input.
    """
    pass

class ParenthesisrError(Exception):
    """Exception Thrown when a open parenthesis doesn't have a closing pair
    or a closing parenthesis is found without an open pair on the stack.

    """
    pass

# pylint: disable=too-few-public-methods
class Token:
    """A class that contains a type and a value. Foundational building block
    of the language typing system.
    """

    # pylint: disable=redefined-builtin
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
    """Class that reads text, which should contain valid pascal programs,
    lexes and parsers then produces line by line results.
    """

    def __init__(self, text: str):
        """
        """
        # Text to be interpreted
        # NOTE: no verification at this point in time.
        self.text = text
        # position of the index on self.text
        self.position = 0
        # current token
        self.current_token = None

    def _error(self) -> None:
        """
        """
        # NOTE: force students to test these kinds of functions so they catch
        # things like mis-namings.
        raise InterpreterError(
            "input_text == {}, current_position == {}".format(
                self.text,
                self.position))

    def _tokenize_integer(self, text: str) -> Token:
        """If have found a single digit then this helper function will read
        characters until the end of the integer is found.
        """
        # NOTE: The first couple attempts at this function were very messed up
        # and screwed up other functionality in the interpreter that my tests
        # caught.

        # First we check to see if there are other digits in the int.
        first_position = self.position
        current_position = self.position
        current_character = text[current_position]

        while True:
            if not current_character.isdigit():
                break

            current_position += 1
            try:
                current_character = text[current_position]
            except IndexError:
                # If we've hit EOF we'll hit this exception.
                break

        # Current position should be EOF or a digit.
        self.position = current_position
        value = int(text[first_position: current_position])
        return Token(INTEGER, value)

    def _consume_whitespace(self, text: str) -> None:
        """Eats all whitespace found until there's nothing left.
        """
        current_position = self.position
        current_character = text[current_position]
        while True:
            if not current_character.isspace():
                break

            current_position += 1
            try:
                current_character = text[current_position]
            except IndexError:
                # If we've hit EOF we'll hit this exception.
                break

        self.position = current_position

    def _next_token(self) -> Token:
        """This is the method that calls the token class and breaks the input
        text into a set of tokens. This set of operations is called lexical
        analyization.
        """
        text = self.text
        return_token = None

        # Check to make sure we haven't run out of characters. If we have,
        # return an EOF token.
        if self.position > len(text) - 1:
            # NOTE: forgot the return statement and test caught it.
            return Token(EOF, None)

        # Get the character that's at the current position.
        current_character = text[self.position]

        if current_character.isspace():
            self._consume_whitespace(text)

            if self.position > len(text) - 1:
                return Token(EOF, None)
            # After we've eatten all the bab whitespace lets actually grab a
            # symantically meaningful character.
            current_character = text[self.position]


        if current_character.isdigit():
            return_token = self._tokenize_integer(text)

        if current_character == "*":
            self.position += 1
            return_token = Token(TIMES, current_character)

        if current_character == "/":
            self.position += 1
            return_token = Token(DIVIDED_BY, current_character)

        if current_character == "+":
            self.position += 1
            return_token = Token(PLUS, current_character)

        if current_character == "-":
            self.position += 1
            return_token = Token(MINUS, current_character)

        if return_token is None:
            self._error()
        else:
            return return_token

    def _consume_token(self, matching_tokens: Token) -> None:
        """consume_token checks the current tokens type with the token type
        that's passed in. If they don't match then an error is raised.

        args:
            matching_tokens: A list of tokens to be tests against to see if
                the current token is any of the expected tokens.
        """
        if self.current_token.type in matching_tokens:
            self.current_token = self._next_token()
        else:
            # Mistake: Accidently named this function self.error()
            self._error()

    # pylint: disable=invalid-name
    def parse(self) -> any:
        """parse consumes all of the tokens found in self.text looking for a
        set of expected tokens. Currently supported token sets are

        INTEGER PLUS INTEGER
        """
        # Just take whatever the first token is.
        self.current_token = self._next_token()

        left = self.current_token
        self._consume_token(INTEGER)

        result = None
        while True:
            op = self.current_token
            expected_operations = [PLUS, MINUS, TIMES, DIVIDED_BY]
            self._consume_token(expected_operations)

            right = self.current_token
            self._consume_token(INTEGER)

            if result is None and op.type in (TIMES, DIVIDED_BY):
                # multiplying or dividing 0 is bad times.
                result = 1


            # Since we now have INTEGER PLUS INTEGER we can add both integer
            # values together.
            # NOTE: when I added the divided by operation symmantics I copied the
            #       multiplication if statement and didn't change it to an elif.
            #       My previous multiplication unit tests pointed out the error.
            if op.type == TIMES:
                result = left.value * right.value
            elif op.type == DIVIDED_BY:
                #  NOTE: When I first made this function I accidently did floating
                #        point division and my unit test cought it.
                result = left.value // right.value
            elif op.type == PLUS:
                result = left.value + right.value
            elif op.type == MINUS:
                result = left.value - right.value
            else:
                self._error()

            left = Token(INTEGER, result)

            # If we run out of input
            if self.current_token.type == EOF:
                self._consume_token(EOF)
                return result


def main():
    """REPL loop"""
    while True:
        try:
            text = input("calc>")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.parse()
        print(result)

if __name__ == "__main__":
    main()
