import pytest
from palindrome import Palindrome

p1 = Palindrome()

def test_true():
    assert p1.palindrome('abba') == True
    assert p1.palindrome('abcba') == True
    assert p1.palindrome('1234321') == True
    assert p1.palindrome('123321') == True
    assert p1.palindrome(')(*&*()') == True
    assert p1.palindrome(')(**()') == True

def test_false():
    assert p1.palindrome('ab') == False
    assert p1.palindrome('abca') == False
    assert p1.palindrome('1234') == False
    assert p1.palindrome('!@#$%^') == False

def test_typeerror():
    with pytest.raises(TypeError) as e_info:
        p1.palindrome(1)
        p1.palindrome(1.0)
        p1.palindrome(123456789010)