import pytest

import interpreter
from interpreter import Token

def test_no_defaults():
    # There's no valid defaults at the moment.
    with pytest.raises(TypeError):
        interpreter.Token()

def test_known_type():
    # There's no valid defaults at the moment.
    token = interpreter.Token(type=interpreter.INTEGER, 2)
    assert token.value = 1
    assert token.type = interpreter.INTEGER

def test_str():
    pass

def test_repr():
    pass
