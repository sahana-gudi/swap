num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"\nBefore swapping: num1 = {num1}, num2 = {num2}")
num1, num2 = num2, num1
print(f"After swapping: num1 = {num1}, num2 = {num2}")