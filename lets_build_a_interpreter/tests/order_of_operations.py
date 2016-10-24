"""Third set of arithmetic features to be added to interpreter. This set of
features requires a decent bit of changes since data needs to be saved from
prior tokens read in.

My first thought is that we'll need to use a heap or stack to make this work.
"""
import pytest

import pascal_interpreter as p_interp

"""
# NOTE: In order to actually get an order of operations to work a data 
# structure will need to be added to save all tokens until EOF is read.
# Then all operations can be carried out in PEMDAS order.
def test_multiplication_before_addition():
    input_text = "3 + 2 * 2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 7

def test_division_before_addition():
    input_text = "3 + 4 / 2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 5

def test_multiplication_before_subtraction():
    input_text = "3 - 2 * 2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == -1

def test_division_before_subtraction():
    input_text = "3 - 4 / 2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 1

# NOTE: Unary numbers are not currently allowed in the interpreter. This
# function is just here as a reminder that we'll want that feature eventually.
def test_parens_around_number():
    pass
"""

def test_parens_blank():
    input_text = "()"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == ""

def test_parens_blank():
    input_text = "(())"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == ""

def test_parens_on_one_statement():
    input_text = "(2 + 2)"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 4

def test_parens_on_one_statement_with_another_statement():
    input_text = "(2 + 2) * 3"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 12

def test_open_no_close():
    with pytest.raises(p_interp.ParenthesisError):
        input_text = "(2 + 2"
        interpreter = p_interp.Interpreter(text=input_text)

def test_extra_open():
    with pytest.raises(p_interp.ParenthesisError):
        input_text = "((2 + 2"
        interpreter = p_interp.Interpreter(text=input_text)
        assert interpreter.parse() == 7

def test_close_no_open():
    with pytest.raises(p_interp.ParenthesisError):
        input_text = "2 + 2)"
        interpreter = p_interp.Interpreter(text=input_text)
