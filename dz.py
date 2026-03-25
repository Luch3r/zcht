class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self._is_borrowed = False

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False

    def return_book(self):
        self._is_borrowed = False

    def get_info(self):
        status = "Выдана" if self._is_borrowed else "Доступна"
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {status}"


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def borrow(self):
        self._is_borrowed = True
        return True

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Размер файла: {self.file_size} МБ"


class AudioBook(Book):
    def __init__(self, title, author, year, duration, narrator):
        super().__init__(title, author, year)
        self.duration = duration
        self.narrator = narrator

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Чтец: {self.narrator}, Длительность: {self.duration} мин"

    def __str__(self):
        return f"Аудиокнига: {self.title} - {self.narrator}"
