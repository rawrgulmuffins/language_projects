import pytest

import pascal_interpreter as augur


def test_interpreter_blank_program():
    input_text = ""
    interp = augur.Interpreter(text=input_text)
    # If this doesn't barf we're good.


def test_interpreter_error_type():
    input_text = ""
    interpreter = augur.Interpreter(text=input_text)
    augur.InterpreterError
    with pytest.raises(augur.InterpreterError):
        interpreter._error()
