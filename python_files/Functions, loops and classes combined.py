# Define a class called "Person" that has three attributes: "name", "age", and "favorite_color"

class Person:
    def __init__ (self, name, age, favorite_color):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color

alice = Person("Alice", 25, "blue")


# Define a function called "create_person" that prompts the user to enter values for a person's name, age, and favorite color,
# and returns a new instance of the Person class with these values.

def create_person():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    favorite_color = input("Please enter your favorite color: ")
    return Person(name, age, favorite_color)

toby = create_person()

print(toby.name, toby.age, toby.favorite_color)






