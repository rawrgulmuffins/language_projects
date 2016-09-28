import pytest

import pascal_interpreter as p_interp


def test_parse_subtraction():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "1-1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 0


def test_parse_subtraction_negative():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "1-2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == -1


def test_parse_addition():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "1+1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 2

def test_parse_multiplication_identity():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "1*1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 1

def test_parse_multiplication_both_positive():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "10*2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 20

"""
def test_parse_multiplication_one_negative():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "10*-2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == -20

def test_parse_multiplication_both_negative():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "-10*-2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 20
"""

def test_parse_division_identity():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "1/1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 1

def test_parse_division_both_positive():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "10/2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 5

def test_parse_division_integer_division():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "10/3"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 3

def test_parse_division_of_zero():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "10/3"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 3

def test_parse_division_of_by_zero():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "10/3"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 3

"""
# NOTE: These functions were originally commented out because I didn't have
#       a unary negative operator at the time. I choose to comment them out
#       because I didn't want failing tests to just show up. Then I have to 
#       remember how many failing tests is "normal" and that's just a path of
#       bad.
def test_parse_division_one_negative():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "10/-2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == -2

def test_parse_division_both_negative():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "-10*-2"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 2
"""

def test_order_of_operations():
    pass
