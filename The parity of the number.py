﻿def check_even_odd():
    user_input = input("Введите число: ")
    
    try:
        number = int(user_input)
    except ValueError:
        print("Ошибка: введено не число")
        return
    
    if number < 0:
        print("Ошибка: введено отрицательное число")
        return
    
    if number % 2 == 0:
        print(f"Число {number} является четным")
    else:
        print(f"Число {number} не является четным")

check_even_odd()