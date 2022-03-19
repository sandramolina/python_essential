# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title

        # TODO: add properties - these ones are called instance attributes because are unique to an instance

        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret" # properties with double underscores are hidden by the interpreter

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price


    def setDiscount(self, amount):
        self._discount = amount #this underscore gives another coders that _discount is only intended to be used internal, should not be accessed outside of the class

# TODO: create some book instances
b1 = Book("War and Peace", "Leo", 1225, 39.99)
b2 = Book("The Catcher in the Rye", "Salinger", 234, 29)

# # TODO: print the price of book1
# print(b1.getPrice())

# # TODO: try setting the discount
# print(b2.getPrice())
# b2.setDiscount(0.25)
# print(b2.getPrice())


# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret) #this one runs
print(b1.__secret)
