﻿имя = input("Ваше имя: ")
фамилия = input("Фамилия: ")
возраст = input("Возраст: ")

# Вывод с использованием метода format()
print("\nРеализация через format:")
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(имя, фамилия, возраст))

# Вывод с использованием f-string
print("\nРеализация через f-string:")
print(f"Ваше имя: {имя}, Фамилия: {фамилия}, Возраст: {возраст} лет")
