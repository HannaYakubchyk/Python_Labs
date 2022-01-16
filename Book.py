import datetime


class Book:
    publisher = "издательство АБВ"
    __year = datetime.datetime.now().year
    coverType = "твердый"
    id = 0

    def __init__(self, name, author, number_of_pages):
        Book.id += 1
        self.name = name
        self.author = author
        self.number_of_pages = number_of_pages

    def get_id(self):
        return self.id

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, publisher):
        self.publisher = publisher

    @staticmethod
    def how_old_is_the_book(year):
        print(f"Книге {datetime.datetime.now().year - year} лет")

    @classmethod
    def current_year_of_publishment(cls):
        print(f"Текущий год печати книг {cls.__year}")

    def show_book_info(self):
        print(f"Автор книги: {self.author}, название книги: {self.name}, год издания: {self.get_year()}, "
              f"издательство: {self.get_publisher()}, переплет: {self.coverType}, id номер: {self.id} ")


book1 = Book("Война и мир", "Толстой", 1225)
book1.set_year(1865)
book1.show_book_info()
book1.how_old_is_the_book(book1.get_year())

book2 = Book("Новая книга", "Иванов", 233)
book2.set_publisher("ВБА")
book2.show_book_info()

Book.how_old_is_the_book(1274)
Book.current_year_of_publishment()
