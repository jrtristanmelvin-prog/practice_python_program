# input 10 numbers
counter = 0

for i in range(10):
    num = float(input("Enter a number: "))

# check if odd
    if num % 2 != 0:

# count
        counter += 1

# print the counter
print(counter)  