try:
    age_input = input("Введите ваш возраст: ")
    age = int(age_input)
    
    if age >= 0:
        if age >= 18:
            print("Вы совершеннолетний.")
        else:
            print("Вы несовершеннолетний.")
    else:
        print("Ошибка: возраст не может быть отрицательным!")
except ValueError:
    print("Ошибка: введено не число!")