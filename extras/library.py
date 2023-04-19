
class library():
    def __init__(self):
        self.users = {}  # dictionary to store users
        self.authors = {}  # dictionary to store authors
        self.books = {}  # dictionary to store book copies
        self.book_loans = {}  # dictionary to store book loans

    def add_user(self, user_name, user_number):
        # """Add a user to the system"""
        self.users[user_name] = user_number

    def return_users(self):
        """Return all associated pieces of information relating to the set of users currently stored in the system"""
        return self.users

    def add_author(self, author_name, author_genre):
        """Add an author to the system"""
        self.authors[author_name] = author_genre

    def return_authors(self):
        """Return all associated pieces of information relating to the set of authors currently stored in the system"""
        return self.authors

    def add_book_copy(self, book_author, book_title):
        """Add a book copy to the system"""
        book_key = (book_author, book_title)
        if book_key not in self.books:
            self.books[book_key] = 1  # initialize number of copies to 1
        else:
            self.books[book_key] += 1  # increment number of copies

    def return_books_not_loan(self):
        """Return all books that are not loaned"""
        books_not_loan = []
        for book_key, num_copies in self.books.items():
            if book_key not in self.book_loans:
                books_not_loan.append(book_key)
        return books_not_loan

    def loan_book(self, user_name, book_title, year, month, day):
        """Loan a book to a user"""
        book_key = None
        for k in self.books.keys():
            if k[1] == book_title:
                book_key = k
                break
        if book_key is None:
            raise ValueError("Book not found")
        if book_key in self.book_loans:
            raise ValueError("Book already loaned")
        self.book_loans[book_key] = (user_name, year, month, day)

    def end_book_loan(self, user_name, book_title, year, month, day):
        """End a book loan"""
        book_key = None
        for k in self.books.keys():
            if k[1] == book_title:
                book_key = k
                break
        if book_key is None:
            raise ValueError("Book not found")
        loan_info = self.book_loans.get(book_key)
        if loan_info is None:
            raise ValueError("Book not loaned")
        if loan_info[0] != user_name:
            raise ValueError("Book not loaned to specified user")
        if loan_info[1:] != (year, month, day):
            raise ValueError("Incorrect end date")

    def delete_book_not_loan(self, book_title):
        """Delete books not in loan"""
        self.return_books_not_loan()

    def user_loans_date(self, user_name, start_year, start_month, start_day, end_yaer, end_month, end_day):
        """filter loan between date"""
        x1 = self.loan_book(self, user_name, 'book_title', start_year, start_month, start_day)
        x2 = self.loan_book(self, user_name, 'book_title_1', end_yaer, end_month, end_day)
        return x1-x2


lib = library()

lib.add_user('user_name', 'user_number')
lib.add_user('user_name_1', 'user_number')
# print(lib.return_users())

lib.add_author('author_name', 'author_genre')
# print(lib.return_authors())

lib.add_book_copy('book_author', 'book_title')
lib.add_book_copy('book_author_1', 'book_title_1')
# print(lib.return_books_not_loan())

lib.loan_book('user_name', 'book_title', 'year', 'month', 'day')
# lib.loan_book('user_name_1', 'book_title_1', 'year', 'month', 'day')

lib.end_book_loan('user_name', 'book_title', 'year', 'month', 'day')
# lib.end_book_loan('user_name_1', 'book_title_1', 'year', 'month', 'day')

# lib.delete_book_not_loan('book_title')
# print(lib.return_books_not_loan())


'''

[('book_author_1', 'book_title_1')]

(
{'user_name': 'user_number', 'user_name_1': 'user_number'}, 

{'author_name': 'author_genre'}, 

{('book_author', 'book_title'): 1, ('book_author_1', 'book_title_1'): 1}, 

{('book_author', 'book_title'): ('user_name', 'year', 'month', 'day')}
)

'''
