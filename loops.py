# Loops in Python

# for loop
print("For loop:")
for i in range(1, 6):
    print("Number:", i)

# while loop
print("\nWhile loop:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Multiplication table
print("\nMultiplication table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Loop with break and continue
print("\nSkip 3, stop at 6:")
for i in range(1, 10):
    if i == 3:
        continue
    if i == 6:
        break
    print(i)
