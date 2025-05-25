def append_to_file(text, filename):
    # Добавляем текст в файл с новой строки
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    
    # Читаем файл и выводим четные строки
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print("Четные строки файла:")
        for index, line in enumerate(lines, start=1):
            if index % 2 == 0:
                print(line.strip())