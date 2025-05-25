import random
from datetime import datetime, timedelta
from array import array

def generate_random_date(start_date, end_date):
    """Генерация случайной даты между start_date и end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def main():
    # Определяем диапазон дат: последние 5 лет от текущей даты
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)

    # Создаем массив для хранения дат в виде строк 'YYYY-MM-DD'
    dates = array('u', [' '] * 10 * 10)  # Каждая дата занимает 10 символов
    date_objects = []

    # Генерируем 10 случайных дат
    for i in range(10):
        random_date = generate_random_date(start_date, end_date)
        date_objects.append(random_date)
        date_str = random_date.strftime('%Y-%m-%d')
        # Записываем дату в массив (каждый символ отдельно)
        for j in range(10):
            dates[i*10 + j] = date_str[j]

    # Преобразуем массив обратно в строки для вывода
    date_strings = []
    for i in range(10):
        date_str = ''.join(dates[i*10 : (i+1)*10])
        date_strings.append(date_str)

    # Вычисляем разницу между соседними датами
    for i in range(9):
        date1 = datetime.strptime(date_strings[i], '%Y-%m-%d')
        date2 = datetime.strptime(date_strings[i+1], '%Y-%m-%d')
        delta = abs((date2 - date1).days)
        print(f"Разница между {date_strings[i]} и {date_strings[i+1]}: {delta} дней")

if __name__ == "__main__":
    main()