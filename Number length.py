while True:
    user_input = input("Введите число: → ")
    
    if user_input == "exit":
        print("Выход из программы...")
        break
    
    if user_input.lstrip('-').isdigit():
        num_digits = len(user_input.lstrip('-'))
        print(f"В этом числе {num_digits} цифры.")
    else:
        print("Ошибка: данные не являются числом.")