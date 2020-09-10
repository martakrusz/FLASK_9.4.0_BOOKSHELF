import json


class Books:
    def __init__(self):
        try:
            with open("books.json", "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def all(self):
        return [book for book in self.books if not book.get('deleted')]

    def get(self, id):
        book = [book for book in self.all() if book['id'] == id and not book.get('deleted')]
        if book:
            return book[0]
        return []

    def create(self, data):
        self.books.append(data)
        self.save_all()

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.books, f)

    def update(self, id, data):
        book = self.get(id)
        if book:
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        book = self.get(id)
        if book:
            book["deleted"]=True
            #self.books.removed(book)
            self.save_all()
            return True
        return False


books = Books()