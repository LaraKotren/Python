input_data = input("Введите числа через пробел: ").split()
power = int(input("Введите степень: "))

result = []

for item in input_data:
    try:
        # Пробуем преобразовать элемент в число
        number = float(item)
        # Проверяем, является ли число целым
        if number.is_integer():
            number = int(number)
        # Возводим в степень
        powered = number ** power
        result.append(str(powered))
    except ValueError:
        # Если не число, умножаем строку на степень
        multiplied_str = item * power
        result.append(multiplied_str)

print("Вывод:", " ".join(result))