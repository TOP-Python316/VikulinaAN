class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def play(self):
        pass

class Drama(Movie):
    def play(self):
        return f"Включаем драму '{self.title}' реж. {self.director}."

class Comedy(Movie):
    def play(self):
        return f"Включаем комедию '{self.title}' реж. {self.director}."

class Horror(Movie):
    def play(self):
        return f"Включаем фильм ужасов '{self.title}' реж. {self.director}."

class Action(Movie):
    def play(self):
        return f"Включаем боевик '{self.title}' реж. {self.director}."

class Romance(Movie):
    def play(self):
        return f"Включаем мелодраму '{self.title}' реж. {self.director}."

class FilmCatalogue:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def play_all_movies(self):
        for movie in self.movies:
            print(movie.play())

    def search_movies_by_genre(self, genre_class):
        return [movie for movie in self.movies if isinstance(movie, genre_class)]

    def play_movies_by_genre(self, genre_class):
        movies = self.search_movies_by_genre(genre_class)
        if movies:
            print(movies[0].play())

# Пример использования
my_catalogue = FilmCatalogue()
my_catalogue.add_movie(Drama("Крестный отец", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Comedy("Ночные игры", "Джон Фрэнсис Дейли, Джонатан М. Голдштейн"))
my_catalogue.add_movie(Horror("Дракула Брэма Стокера", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Action("Крушение", "Жан-Франсуа Рише"))
my_catalogue.add_movie(Romance("Честная куртизанка", "Маршалл Херсковиц"))

my_catalogue.play_all_movies()

print("\nНайдены фильмы ужасов:")
for movie in my_catalogue.search_movies_by_genre(Horror):
    print(movie.title)

print("\nЗапускаем фильм из жанра 'Мелодрамы':")
my_catalogue.play_movies_by_genre(Romance)
