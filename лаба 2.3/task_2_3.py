class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Book: {self.name} by {self.author}"

    def __repr__(self):
        return f"Book(name={self.name}, author={self.author})"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = value

    def __str__(self):
        return f"PaperBook: {self.name} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"PaperBook(name={self.name}, author={self.author}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Duration must be a positive float")
        self._duration = value

    def __str__(self):
        return f"AudioBook: {self.name} by {self.author}, {self.duration} hours"

    def __repr__(self):
        return f"AudioBook(name={self.name}, author={self.author}, duration={self.duration})"


# Пример использования
if __name__ == "__main__":
    book = Book("1984", "George Orwell")
    print(book)
    print(repr(book))

    paper_book = PaperBook("1984", "George Orwell", 328)
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook("1984", "George Orwell", 11.5)
    print(audio_book)
    print(repr(audio_book))