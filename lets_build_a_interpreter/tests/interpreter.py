import pytest

import pascal_interpreter as p_interp


def test_interpreter_blank_program():
    input_text = ""
    interp = p_interp.Interpreter(text=input_text)
    # If this doesn't barf we're good.


def test_interpreter_error_type():
    input_text = ""
    interpreter = p_interp.Interpreter(text=input_text)
    p_interp.InterpreterError
    with pytest.raises(p_interp.InterpreterError):
        interpreter._error()
