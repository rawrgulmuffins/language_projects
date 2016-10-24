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

def test_next_token_is_minus():
    input_text = "-"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter._next_token().type == p_interp.MINUS

def test_next_token_is_plus():
    input_text = "+"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter._next_token().type == p_interp.PLUS

def test_next_token_is_multipe_digit_int():
    input_text = "12"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter._next_token().type == p_interp.INTEGER

def test_next_token_is_int():
    input_text = "1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter._next_token().type == p_interp.INTEGER

def test_next_token_read_full_int():
    input_text = "12"
    interpreter = p_interp.Interpreter(text=input_text)
    #import pdb; pdb.set_trace()
    token = interpreter._next_token()
    assert token.type == p_interp.INTEGER
    assert token.value == 12
    assert interpreter._next_token().type == p_interp.EOF

def test_eof_token_after_int():
    input_text = "1"
    interpreter = p_interp.Interpreter(text=input_text)
    token = interpreter._next_token()
    assert token.type == p_interp.INTEGER
    assert token.value == 1
    assert interpreter._next_token().type == p_interp.EOF

def test_consume_valid_token():
    input_text = "1+1"
    interpreter = p_interp.Interpreter(text=input_text)

    # Mistake: Since _next_token changes the state of position you can't just
    # interpreter.current_token = p_interp.Token(p_interp.INTEGER, 1)
    # You have to call _next_token.

    interpreter.current_token = interpreter._next_token()

    # Mistake 2: this unit test caught me breaking single digit integers when
    # I added double digit.

    interpreter._consume_token(p_interp.INTEGER)
    assert interpreter.position == 2 # Make sure we haven't skipped past the +
    assert interpreter.current_token.type == p_interp.PLUS

def test_consume_valid_token_from_list():
    input_text = "1-1"
    interpreter = p_interp.Interpreter(text=input_text)
    interpreter.current_token = interpreter._next_token()
    token_list = [p_interp.INTEGER, p_interp.MINUS]
    interpreter._consume_token(token_list)
    assert interpreter.position == 2 # Make sure we haven't skipped past the +
    assert interpreter.current_token.type == p_interp.MINUS

def test_consume_invalid_token():
    input_text = "+1"
    interpreter = p_interp.Interpreter(text=input_text)
    interpreter.current_token = interpreter._next_token()
    with pytest.raises(p_interp.InterpreterError):
        interpreter._consume_token(p_interp.INTEGER)

def test_parse_addition_with_internal_spaces():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "1 +1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 2

def test_parse_addition_with_trailing_spaces():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "1+1 "
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 2

def test_parse_addition_with_pre_spaces():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = " 1+1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 2

def test_parse_addition_with_all_combinations_spaces():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = " 1 + 1 "
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 2

def test_parse_addition_multiple_digits():
    input_text = "12+1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 13

def test_parse_sets_eof():
    input_text = "1+1"
    interpreter = p_interp.Interpreter(text=input_text)
    interpreter.parse()
    assert interpreter.current_token.type == p_interp.EOF

def test_parse_invalid_addition():
    input_text = "+1"
    interpreter = p_interp.Interpreter(text=input_text)
    with pytest.raises(p_interp.InterpreterError):
        interpreter.parse()
