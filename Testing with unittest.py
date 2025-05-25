import unittest
import sys
from your_module import factorial  # Замените `your_module` на имя модуля, где находится функция factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
    
    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-5)
    
    def test_factorial_overflow(self):
        # Найдем граничное значение, где factorial еще не вызывает переполнение
        n = 1
        while True:
            try:
                factorial(n)
                n += 1
            except ValueError:
                break
        # Проверяем, что для n-1 факториал считается, а для n - уже переполнение
        self.assertTrue(factorial(n - 1) > 0)
        with self.assertRaises(ValueError):
            factorial(n)
    
    def test_factorial_of_large_but_supported_number(self):
        # Проверяем, что функция корректно работает для больших, но допустимых значений
        # Например, факториал 20 должен быть посчитан
        self.assertEqual(factorial(20), 2432902008176640000)
    
    def test_factorial_input_type(self):
        # Проверяем, что функция принимает только целые числа
        with self.assertRaises(TypeError):
            factorial(5.5)
        with self.assertRaises(TypeError):
            factorial("5")

if __name__ == '__main__':
    unittest.main()