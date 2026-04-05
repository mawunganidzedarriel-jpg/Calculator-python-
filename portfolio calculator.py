Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
op = input("choose +, -, *, /, %: ")

if op == "+":
    print(Num1 + Num2)
elif op == "-":
    print(Num1 - Num2)
elif op == "*":
    print(Num1 * Num2)
elif op == "/":
    print(Num1 / Num2)
elif op == "%":
    print(Num1 % Num2)
else:
    print("Invalid stupid")