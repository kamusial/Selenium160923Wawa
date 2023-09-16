# import pytest_funkcje
# pytest_funkcje.dodawanie()

from pytest_funkcje import *
import pytest

# def test_dodawanie1():
# #     assert dodawanie(3, 5) == 8
# #     assert dodawanie(3, 2) == 8
# #
# # def test_dodawanie2():
# #     assert dodawanie(1, 1) == 2

# def test_mnozenie():
#     assert mnozenie(10, 5) == 50
#     assert mnozenie(10, 1.1) == 11
#     assert mnozenie(100, 1.1) == 110
#     assert mnozenie(2, 'mama') == 'mamamama'

def test_fissbuzz_basic():
    assert fissbuzz(1) == 1
    assert fissbuzz(2) == 2
    assert fissbuzz(3) == 'fiss'
    assert fissbuzz(5) == 'buzz'
    assert fissbuzz(9) == 'fiss'
    assert fissbuzz(15) == 'fissbuzz'

def test_fissbuzz_advanced():
    assert fissbuzz(0) == None
    assert fissbuzz(-5) == None
    assert fissbuzz('mama' == None)
    assert fissbuzz(5.8) == 'buzz'


