import pytest
from wordCount import wordCount

w1 = wordCount()

def test_true():
    assert w1.wordCount('Hello') == 1
    assert w1.wordCount('My name is.') == 3
    assert w1.wordCount('One Two Three Four Five.') == 5

def test_typeerror():
    with pytest.raises(TypeError) as e_info:
        w1.wordCount(1)
        w1.wordCount(1.0)
        w1.wordCount(123456789010)
