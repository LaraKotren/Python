import math

def prime_numbers():
    num = 2
    while True:
        is_prime = True
        # Проверяем делители от 2 до квадратного корня из num
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

primes = prime_numbers()
for _ in range(10):
    print(next(primes))