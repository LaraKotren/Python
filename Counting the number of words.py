text = input("Введите строку: ").lower().split()  

# Создаём пустой словарь для хранения количества повторений каждого слова
word_counts = {}  

for word in text:  
    if word in word_counts:  
        word_counts[word] += 1  
    else:  
        word_counts[word] = 1  

# Выводим результат в формате "слово: количество повторений"
for word, count in word_counts.items():  
    print(f"{word}: {count}")  