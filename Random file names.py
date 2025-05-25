import random
import string
from pathlib import Path

def generate_random_filename(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length)) + '.txt'

def create_random_files(directory, count=10):
    directory_path = Path(directory)
    directory_path.mkdir(parents=True, exist_ok=True)  # Создаем директорию, если её нет
    
    created_files = []
    for _ in range(count):
        filename = generate_random_filename()
        file_path = directory_path / filename
        file_path.touch()  # Создаем пустой файл
        created_files.append(file_path)
    
    return created_files

# Укажите путь к директории, где нужно создать файлы
target_directory = "random_files"

# Создаем файлы и получаем их пути
created_files = create_random_files(target_directory)

# Выводим абсолютные пути созданных файлов
for file_path in created_files:
    print(file_path.absolute())