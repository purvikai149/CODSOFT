print("Welcome to my calculator")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Pick operation:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

ch = input("Enter choice: ")

if ch == '1':
    print("Answer:", x + y)
elif ch == '2':
    print("Answer:", x - y)
elif ch == '3':
    print("Answer:", x * y)
elif ch == '4':
    if y != 0:
        print("Answer:", x / y)
    else:
        print("Cannot divide by zero.")
else:
    print("Wrong input")
