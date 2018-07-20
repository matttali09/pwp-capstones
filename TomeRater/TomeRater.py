class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "The users email has been changed to %s" %self.email

    def __repr__(self):
        return "User: %s, email: %s, books read = %r" %(self.name, self.email, len(self.books))

    def __eq__(self, other):
        return self.value == other

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        for rating in self.books.values():
            if rating != None:
                average += rating
        return average / len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        return self.isbn == new_isbn

    def add_rating(self, rating):
        if rating is not None and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            return "Invalid Rating"

    def __eq__(self, other):
        return self.value == other

    def get_average_rating(self):
        average = 0
        for rating in self.ratings:
            average += rating
        return average / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "%s by %s" %(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "%s, a %s manual on %s" %(self.title, self.level, self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_book = Fiction(title, author, isbn)
        return new_book

    def create_non_fiction(self, title, author, level, isbn):
        new_book = Non_Fiction(title, author, level, isbn)
        return new_book

    def add_book_to_user(self, book, email, rating = None):
        if email not in self.users:
            print("No user with email {}".format(email))
        else:
          self.users[email].read_book(book, rating)
          book.add_rating(rating)
        if book not in self.books:
            self.books[book] = 1
        else:
            self.books[book] += 1

    def add_user(self, name, email, books = None):
        user = User(name, email)
        self.users[email] = user
        if books != None:
            for book in books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        book = self.books.keys()
        print(book)

    def print_users(self):
        user = self.users.values()
        print(user)

    def most_read_book(self):
        maximum = max(self.books, key = self.books.get)
        print("{} has been read {} times.".format(maximum, self.books[maximum]))

    def highest_rated_book(self):
        ratings = {}
        for book in self.books:
            ratings[book] = book.get_average_rating()
        maximum = max(ratings, key = ratings.get)
        print("Book: %r\nScore: %r" %(maximum, ratings[maximum]))

    def most_positive_user(self):
        ratings = {}
        for user in self.users.values():
            ratings[user.name] = user.get_average_rating()
        maximum = max(ratings, key = ratings.get)
        print("User: %r\nScore: %r" %(maximum, ratings[maximum]))
