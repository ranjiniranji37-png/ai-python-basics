# Lists in Python

fruits = ["apple", "banana", "mango"]
print("Original list:", fruits)

fruits.append("orange")
fruits.insert(1, "grapes")
print("After adding:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Length:", len(fruits))

# Sorting
fruits.sort()
print("Sorted:", fruits)

# Looping through a list
for f in fruits:
    print("Fruit:", f)

# List of numbers
numbers = [4, 8, 15, 16, 23, 42]
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Squares:", [n ** 2 for n in numbers])
