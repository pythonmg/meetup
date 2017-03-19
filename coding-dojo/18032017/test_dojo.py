"""

Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:
Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
"""
from dojo import FizzBuzz, FizzBuzzList

def test_number_3():
    assert FizzBuzz(3) == "Fizz"

def test_number_5():
    assert FizzBuzz(5) == "Buzz"

def test_number_15():
    assert FizzBuzz(15) == "FizzBuzz"

def test_number_6():
    assert FizzBuzz(6) == "Fizz"

def test_number_10():
    assert FizzBuzz(10) == "Buzz"

def test_number_30():
    assert FizzBuzz(30) == "FizzBuzz"

def test_number_59():
    assert FizzBuzz(59) == "59"

def test_list_at_5():
    assert FizzBuzzList(5) == ["1", "2", "Fizz", "4", "Buzz"]

def test_list_at_15():
    assert FizzBuzzList(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]