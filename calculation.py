a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum=a+b
sub=a-b
mul=a*b
div=a/b
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Error: Division by zero")
