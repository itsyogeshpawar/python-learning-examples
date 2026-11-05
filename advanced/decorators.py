# Decorators in Python
# Functions that modify other functions.

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Explanation:
# - Decorators wrap functions to add behavior.
# - Use @decorator_name above a function to apply it.
