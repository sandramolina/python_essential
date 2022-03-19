# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class book:
    def __init__(self, title):
        self.title = title

# TODO: create instances of the class
b1 = book("Brave New World")
b2 = book("Pride and Predujice")

# TODO: print the class and property
print(b1)
print(type(b1))
print(f'books are {b1.title} and {b2.title}')