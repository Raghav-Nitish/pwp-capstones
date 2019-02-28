#Vobbalareddy Raghav Nitish Chandra
#TomeRater Capstone Project
#April 2, 2019
#This project allows users to read and rate books

class User(object):
    def __init__(self, name, email):
        if ("@") and (".com" or ".org" or ".edu") in email:
            self.name = name
            self.email = email
            self.books = {}
        else:
            print("Invalid email address! User cannot be created.")

    def get_email(self):
        return self.email

    def change_email(self, address):
        if ("@") and (".com" or ".org" or ".edu") in address:
            self.email = address 
            print("Your email has been updated!")
        else:
            print("Email address cannot be changed because it has an invalid format.")

    def __repr__(self):
        return "User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            print("Both user objects are equal!")
        else:
            print("The user objects are not equal.")
            
    def read_book(self, book, rating=None):
        self.books[book] = rating
        
    def get_average_rating(self):
        total_sum = 0

        for i in self.books.values():
            total_sum += i
            
        return total_sum / len(self.books)
            
class Book:
    def __init__(self, title, isbn):      
        isbn_list = []
        self.isbn = isbn
        
        if self.isbn in isbn_list:
            print("Cannot add this book since the book's ISBN is not unique.")
        else:
            self.title = title
            self.ratings = []
            isbn_list.append(self.isbn)
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's ISBN has been updated!")
        
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)    
        else:
            print("Invalid Rating")
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            print("Both book objects are equal!")
        else:
            print("The book objects are not equal.")
            
    def get_average_rating(self):
        total_sum_1 = 0
        
        for i in self.ratings:
            total_sum_1 += i
            
        return total_sum_1 / len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return self.title + " by " + self.author
    
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
        return self.title + " a " + self.level + " manual on " + self.subject
        
class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self, title, isbn):
        new_book_object = Book(title, isbn)
        return new_book_object
    
    def create_novel(self, title, author, isbn):
        new_fiction_book_object = Fiction(title, author, isbn)
        return new_fiction_book_object
    
    def create_non_fiction(self, title, subject, level, isbn):
        new_nonfiction_book_object = Non_Fiction(title, subject, level, isbn)
        return new_nonfiction_book_object
    
    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            (self.users[email]).read_book(book, rating)
            book.add_rating(rating)          
            
            if book in self.books:
                temp_val = self.books[book]
                self.books[book] = temp_val + 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}".format(email=email))
    
    def add_user(self, name, email, user_books=None):
        if email in self.users:
            print("Sorry! This user already exists. You can't add him/her!")
        else:
            new_user_object = User(name, email)
            
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)
                
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
        for user in self.users.values():
            print(user)
            
    def most_read_book(self):
        largest_value = float("-inf")
        for key, value in self.books.items():
            if value > largest_value:
                largest_value = value
                mostreadbook = key       
        return mostreadbook
    
    def highest_rated_book(self):
        highest_rating = 0
        for book in self.books.keys():
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highestratedbook = book
        return highestratedbook
    
    def most_positive_user(self):
        highest_rating_1 = 0
        for user in self.users.values():
            if user.get_average_rating() > highest_rating_1:
                highest_rating_1 = user.get_average_rating()
                highestrateduser = user
        return highestrateduser