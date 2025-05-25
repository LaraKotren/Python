import random
import math
import statistics

numbers = [random.randint(1, 100) for _ in range(100)]

mean = statistics.mean(numbers)  # Среднее арифметическое
median = statistics.median(numbers)  # Медиана
stdev = statistics.stdev(numbers)  # Стандартное отклонение
sqrt_sum = math.sqrt(sum(numbers))  # Квадратный корень из суммы
rounded_sqrt = round(sqrt_sum, 2)  # Округление до двух знаков после запятой

print(f"Среднее: {mean:.2f}, Медиана: {median}, Стандартное отклонение: {stdev:.2f}, Корень из суммы: {rounded_sqrt:.2f}")