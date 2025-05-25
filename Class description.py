class Movie:
    # Атрибуты класса
    rating_system = "IMDb"
    max_rating = 10.0

    def __init__(self, title: str, director: str, year: int, genre: str, duration: int) -> None:
        # Атрибуты объекта
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration  # в минутах
        self.rating = 0.0  # начальный рейтинг

    def __str__(self) -> str:
        return f"'{self.title}' ({self.year}), реж. {self.director}, {self.genre}"

    def set_rating(self, new_rating: float) -> None:
        """Устанавливает рейтинг фильма"""
        if 0 <= new_rating <= self.max_rating:
            self.rating = new_rating
        else:
            print(f"Рейтинг должен быть от 0 до {self.max_rating}")

    def is_long(self) -> bool:
        """Проверяет, считается ли фильм длинным (более 2 часов)"""
        return self.duration > 120

    def get_age(self, current_year: int) -> int:
        """Возвращает возраст фильма"""
        return current_year - self.year

    def add_genre(self, additional_genre: str) -> None:
        """Добавляет дополнительный жанр к фильму"""
        self.genre += f", {additional_genre}"


# Создаем объекты
movie1 = Movie("Крестный отец", "Фрэнсис Форд Коппола", 1972, "Криминал, драма", 175)
movie2 = Movie("Назад в будущее", "Роберт Земекис", 1985, "Фантастика, комедия", 116)

# Работаем с объектами
print(movie1)  # Используется переопределенный __str__
print(f"Фильму {movie1.title} {movie1.get_age(2025)} лет")

movie2.set_rating(8.5)
print(f"Рейтинг фильма '{movie2.title}': {movie2.rating}")

print(f"Фильм '{movie1.title}' длинный? {movie1.is_long()}")
print(f"Фильм '{movie2.title}' длинный? {movie2.is_long()}")

movie1.add_genre("боевик")
print(f"Обновленные жанры '{movie1.title}': {movie1.genre}")

# Изменяем атрибут класса
Movie.rating_system = "Кинопоиск"
print(f"Система рейтинга изменена на: {Movie.rating_system}")