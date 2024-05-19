class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def play(self):
        pass

class Drama(Movie):
    def play(self):
        return f"�������� ����� '{self.title}' ���. {self.director}."

class Comedy(Movie):
    def play(self):
        return f"�������� ������� '{self.title}' ���. {self.director}."

class Horror(Movie):
    def play(self):
        return f"�������� ����� ������ '{self.title}' ���. {self.director}."

class Action(Movie):
    def play(self):
        return f"�������� ������ '{self.title}' ���. {self.director}."

class Romance(Movie):
    def play(self):
        return f"�������� ��������� '{self.title}' ���. {self.director}."

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

# ������ �������������
my_catalogue = FilmCatalogue()
my_catalogue.add_movie(Drama("�������� ����", "������� �. �������"))
my_catalogue.add_movie(Comedy("������ ����", "���� ������� �����, �������� �. ���������"))
my_catalogue.add_movie(Horror("������� ����� �������", "������� �. �������"))
my_catalogue.add_movie(Action("��������", "���-������� ����"))
my_catalogue.add_movie(Romance("������� ����������", "������� ���������"))

my_catalogue.play_all_movies()

print("\n������� ������ ������:")
for movie in my_catalogue.search_movies_by_genre(Horror):
    print(movie.title)

print("\n��������� ����� �� ����� '���������':")
my_catalogue.play_movies_by_genre(Romance)
