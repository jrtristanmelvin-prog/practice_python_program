#input num1 and num2 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#compare the 2 numbers and print the bigger number 
if num1 > num2: 
    print(f"The bigger number is: {num1}" )
elif num1 == num2:
    print(f"Both numbers are equal")
else:
    print(f"The bigger number is: {num2}")