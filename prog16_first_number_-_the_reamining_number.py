# input first number
num1 = float(input("Enter number 1: "))

# input the 9 numbers and subract it from num1 
for i in range(2,11):
    nums = float(input(f"Enter number {i}: "))
    num1 = num1 - nums

# print the result
print(f"The result is: {num1}")