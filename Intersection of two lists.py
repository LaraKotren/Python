# Ввод данных
list1 = input("Введите первый список: ").split()
list2 = input("Введите второй список: ").split()

# Преобразование в множества и нахождение пересечения
common_elements = set(list1) & set(list2)

# Вывод результата
print("Общие элементы:", ' '.join(common_elements))