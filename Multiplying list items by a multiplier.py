from typing import List, TypeVar, Union

T = TypeVar('T', int, float, str)

def multiply_list_elements(elements: List[T], multiplier: Union[int, float] = 2) -> List[T]:
    return [element * multiplier for element in elements]

# Лямбда-функция для той же операции
lambda_multiply = lambda lst, m=2: list(map(lambda x: x * m, lst))

# Пример работы с пользовательским вводом
if __name__ == "__main__":
    input_list = input("Введите список чисел через пробел: ").split()
    try:
        numbers = [int(num) for num in input_list]
    except ValueError:
        try:
            numbers = [float(num) for num in input_list]
        except ValueError:
            numbers = input_list  # если не числа, работаем со строками
    
    multiplier_input = input("Введите множитель (по умолчанию 2): ")
    multiplier = float(multiplier_input) if multiplier_input else 2
    
    # Для строк множитель должен быть целым
    if isinstance(numbers[0], str) and not multiplier_input.isdigit():
        multiplier = 2
    
    print(f"Результат (функция): {multiply_list_elements(numbers, multiplier)}")
    print(f"Результат (лямбда-функция): {lambda_multiply(numbers, multiplier)}")