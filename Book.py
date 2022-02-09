import datetime
import itertools


class Book:
    publisher = "издательство АБВ"
    __year = datetime.datetime.now().year
    coverType = "твердый"
    __id = itertools.count(1, 1)

    def __init__(self, name, author, number_of_pages):
        self.__id = next(Book.__id)
        self.name = name
        self.author = author
        self.number_of_pages = number_of_pages
        self.price = number_of_pages / 2

    def get_id(self):
        return self.__id

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
              f"издательство: {self.get_publisher()}, переплет: {self.coverType}, цена: {self.price}, "
              f"страниц: {self.number_of_pages}, id номер: {self.__id} ")

    # сравнивает количество страниц в книгах
    def __cmp__(self, other):
        if self.number_of_pages > other.number_of_pages:
            print("В книге " + self.name + " страниц больше, чем в книге " + other.name + ".")
        elif self.number_of_pages < other.number_of_pages:
            print("В книге " + self.name + " страниц меньше, чем в книге " + other.name + ".")
        else:
            print("В обеих книгах одинаковое количество страниц.")

    def __str__(self):
        print(f"Объект с id {self.__id}")


book1 = Book("Война и мир", "Толстой", 1225)
book1.set_year(1865)
book1.show_book_info()
book1.how_old_is_the_book(book1.get_year())

book2 = Book("Мастер и Маргарита", "Булгаков", 504)
book2.set_publisher("ВБА")
book2.show_book_info()

book3 = Book("Мертвые души", "Гоголь", 352)
book3.show_book_info()

Book.how_old_is_the_book(1274)
Book.current_year_of_publishment()

print(book1.get_id())
print(book2.get_id())


Book.__cmp__(book1, book2)
Book.__cmp__(book2, book3)


Book.__str__(book2)
