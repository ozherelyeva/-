class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Пример использования
if __name__ == "__main__":
    # Создаем несколько книг
    book1 = Book(id_=1, name="1984", pages=328)
    book2 = Book(id_=2, name="О дивный новый мир", pages=288)

    # Создаем библиотеку и добавляем книги
    library = Library()
    library.books.append(book1)
    library.books.append(book2)

    # Выводим информацию о книгах
    print(book1)  # Книга "1984"
    print(book2)  # Книга "О дивный новый мир"

    # Получаем следующий ID для новой книги
    next_id = library.get_next_book_id()
    print(f"Следующий ID для новой книги: {next_id}")  # Следующий ID для новой книги: 3

    # Получаем индекс книги по ID
    try:
        index = library.get_index_by_book_id(2)
        print(f"Индекс книги с ID 2: {index}")  # Индекс книги с ID 2: 1
    except ValueError as e:
        print(e)

    # Попытка получить индекс несуществующей книги
    try:
        index = library.get_index_by_book_id(99)
    except ValueError as e:
        print(e)  # Книги с запрашиваемым id не существует
