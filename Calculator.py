import math
import statistics

def addition():
    a = input("Слагаемое 1: ")
    b = input("Слагаемое 2: ")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError("Оба аргумента должны быть числами")
    return a + b

def subtraction():
    a = input("Уменьшаемое: ")
    b = input("Вычитаемое: ")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError("Оба аргумента должны быть числами")
    return a - b

def multiplication():
    a = input("Множитель 1: ")
    b = input("Множитель 2: ")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError("Оба аргумента должны быть числами")
    return a * b

def division():
    a = input("Делимое: ")
    b = input("Делитель: ")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Делитель не может быть нулем")
    
    print("Выберите тип деления:")
    print("1. Обычное деление")
    print("2. Целочисленное деление")
    print("3. Остаток от деления")
    choice = input("Ваш выбор (1-3): ")
    
    if choice == '1':
        return a / b
    elif choice == '2':
        return a // b
    elif choice == '3':
        return a % b
    else:
        raise ValueError("Неверный выбор типа деления")

def power():
    a = input("Основание: ")
    b = input("Степень: ")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError("Оба аргумента должны быть числами")
    return a ** b

def factorial():
    n = input("Число: ")
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Аргумент должен быть целым числом")
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    return math.factorial(n)

def sine():
    a = input("Угол в градусах: ")
    try:
        a = float(a)
    except ValueError:
        raise ValueError("Аргумент должен быть числом")
    return math.sin(math.radians(a))

def median():
    nums = input("Список чисел через пробел: ")
    try:
        nums = list(map(float, nums.split()))
    except ValueError:
        raise ValueError("Все элементы должны быть числами")
    if len(nums) == 0:
        raise ValueError("Список чисел не может быть пустым")
    return statistics.median(nums)

def calculator():
    operations = {
        '1': ('Сложение', addition),
        '2': ('Вычитание', subtraction),
        '3': ('Умножение', multiplication),
        '4': ('Деление', division),
        '5': ('Возведение в степень', power),
        '6': ('Факториал', factorial),
        '7': ('Синус', sine),
        '8': ('Медиана', median)
    }
    
    while True:
        print("\nДоступные операции:")
        for key in operations:
            print(f"{key}. {operations[key][0]}")
        print("--------------------")
        
        operation = input("Операция (или 'exit' для выхода): ")
        if operation.lower() == 'exit':
            break
            
        if operation not in operations:
            print("Неверный выбор операции!")
            continue
            
        try:
            result = operations[operation][1]()
            print(f">>> {result}")
        except Exception as e:
            print(f"Ошибка: {e}")
        print("--------------------")

if __name__ == "__main__":
    calculator()