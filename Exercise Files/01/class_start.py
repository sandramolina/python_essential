# Python Object Oriented Programming by Joe Marini course example
# Using class-level (as opposite to the instance classes), and static methods 


from inspect import classify_class_attrs


class Book:
    # TODO: Properties defined at the class level are shared by all instances (and also the class itself.)
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK") #in uppercase becasue it's a class-level property
    
    # TODO: double-underscore properties are hidden from other classes
    __bookList = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method - we use static methods when we want to make a class callable and not have its state modified
    @staticmethod
    def getBookList():
        if Book.__bookList == None:
            Book.__bookList = []
        return Book.__bookList

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid type of book')
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book types: ", Book.getBookTypes())

# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "EBOOK")

# TODO: Use the static method to access a singleton object (only one instance of a particular variable or object is ever created)
theBooks = Book.getBookList()
theBooks.append(b1.title)
theBooks.append(b2)
print(theBooks)