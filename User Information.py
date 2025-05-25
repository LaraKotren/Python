import random
import json
import string

def generate_random_name():
    first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Robert", "Lisa", "William", "Emma"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Wilson"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_email(name):
    domains = ["example.com", "mail.com", "test.org", "demo.net", "sample.edu"]
    local_part = name.lower().replace(" ", ".") + str(random.randint(1, 99))
    return f"{local_part}@{random.choice(domains)}"

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_user_data():
    name = generate_random_name()
    age = random.randint(18, 80)
    email = generate_random_email(name)
    password = generate_random_password()
    
    return {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }

def save_to_json(data, filename="user_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def read_from_json(filename="user_data.json"):
    with open(filename, 'r') as f:
        return json.load(f)

# Генерация данных пользователя
user_data = generate_user_data()

# Сохранение в файл
save_to_json(user_data)

# Чтение из файла и вывод
loaded_data = read_from_json()
print(json.dumps(loaded_data, indent=4))