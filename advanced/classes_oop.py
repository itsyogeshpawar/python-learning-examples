# Classes and Object-Oriented Programming in Python

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

animal = Animal("Generic Animal")
animal.speak()
dog = Dog("Buddy")
dog.speak()

# Explanation:
# - Classes are defined with 'class'.
# - __init__ is the constructor method.
# - Inheritance allows Dog to extend Animal.
# - Methods are functions inside classes.
