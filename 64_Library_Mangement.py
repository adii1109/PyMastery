"""
Write a Library class with no_of_books and books as instance variable. Write a program to create 
a library from this library class and show how you can print all books , add a book and 
get the number of books using different methods. Show that your program doesnt persist the books  after the program is stopped
""" 


class library:

    def __init__(self) :
        self.NoOfBooks=0
        self.BookName=[]

    def addBook(self,books):
        self.BookName.append(books)
        self.NoOfBooks=len(self.BookName)
    
    def ShowInfo(self):
        print(f"The library has {self.NoOfBooks} has")
        for book in self.BookName:
            print(book)

l1=library()

l1.addBook("harry Potter")
l1.addBook('atomic Habit')
l1.ShowInfo()