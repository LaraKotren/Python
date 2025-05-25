import re

def is_palindrome(s):
    # Приводим строку к нижнему регистру, удаляем все символы, кроме букв и цифр
    cleaned = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', s.lower())
    return cleaned == cleaned[::-1]

# Тесты
assert is_palindrome("Лёша на полке клопа нашёл") == True  # Палиндром с пробелами и пунктуацией
assert is_palindrome("А роза упала на лапу Азора") == True  # Еще один палиндром
assert is_palindrome("racecar") == True  # Английский палиндром без пробелов
assert is_palindrome("hello") == False  # Не палиндром
assert is_palindrome("12321") == True  # Числовой палиндром
assert is_palindrome("") == True  # Пустая строка считается палиндромом