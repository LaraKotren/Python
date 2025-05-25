from math import factorial

# 1. Список квадратов первых 10 натуральных чисел
squares = [x**2 for x in range(1, 11)]
print(f"1. {squares}")

# 2. Словарь дней недели
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekday_dict = {day: i+1 for i, day in enumerate(weekdays)}
print(f"2. {weekday_dict}")

# 3. Множество тегов библиотек в нижнем регистре
libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags = {lib.lower() for lib in libs}
print(f"3. {tags}")

# 4. Список четных чисел
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
evens = [x for x in numbers if x % 2 == 0]
print(f"4. {evens}")

# 5. Словарь факториалов
factorials = {n: factorial(n) for n in range(1, 6)}
print(f"5. {factorials}")