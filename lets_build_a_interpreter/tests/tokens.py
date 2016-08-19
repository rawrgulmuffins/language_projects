"""

NOTE: There are no tests that check for data validation at this point since
the interpreter doesn't have any data validation as a feature.
"""
import pytest

import interpreter
from interpreter import Token

def test_no_defaults():
    # There's no valid defaults at the moment.
    with pytest.raises(TypeError):
        interpreter.Token()

def test_known_type():
    # There's no valid defaults at the moment.
    token = interpreter.Token(type=interpreter.INTEGER, value=2)
    assert token.value == 2
    assert token.type == interpreter.INTEGER

def test_str_non_string_value():
    token = interpreter.Token(type=interpreter.INTEGER, value=2)
    expected_result = "Token(type=INTEGER, value=2)"
    assert token.__str__() == expected_result

def test_repr():
    token = interpreter.Token(type=interpreter.INTEGER, value=2)
    expected_result = "Token(type=INTEGER, value=2)"
    assert token.__repr__() == expected_result
