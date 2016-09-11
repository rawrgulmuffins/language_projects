import pytest

import pascal_interpreter as p_interp


def test_interpreter_blank_program():
    input_text = ""
    interp = p_interp.Interpreter(text=input_text)
    # If this doesn't barf we're good.


def test_interpreter_error_type():
    input_text = ""
    interpreter = p_interp.Interpreter(text=input_text)
    with pytest.raises(p_interp.InterpreterError):
        interpreter._error()


def test_invalid_string_errors():
    input_text = "This is currently an error"
    interpreter = p_interp.Interpreter(text=input_text)
    with pytest.raises(p_interp.InterpreterError):
        interpreter._next_token()


def test_eof_token_at_end_of_line():
    input_text = ""
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter._next_token().type == p_interp.EOF


def test_eof_token_after_int():
    input_text = "1"
    interpreter = p_interp.Interpreter(text=input_text)
    token = interpreter._next_token()
    assert token.type == p_interp.INTEGER
    assert token.value == 1
    assert interpreter._next_token().type == p_interp.EOF
