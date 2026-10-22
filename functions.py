# Functions in Python

def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n):
    return n % 2 == 0


def greet_with_default(name="Intern"):
    return f"Welcome, {name}!"


print(greet("Ranjini"))
print("Sum:", add(5, 3))
print("Factorial of 5:", factorial(5))
print("Is 10 even?", is_even(10))
print(greet_with_default())
