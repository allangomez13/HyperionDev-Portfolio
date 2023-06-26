def calculator():
    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
        
    op = input("Enter the operation(+, -, *,/): ")

    result = 0

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2

    print("The result is: ", result)
    with open("calculations.txt", "a") as file:
        file.write(f"{num1} {op} {num2} = {result}\n")

def read_file():
    while True:
        filename = input("Enter the name of the file: ")
        try:
            with open(filename, "r") as file:
                for line in file:
                    print(line.strip())
            break
        except FileNotFoundError:
            print("File not found. Please try again.")

while True:
    choice = input("Enter 1 to perform a calculation, 2 to read a file, or 3 to exit: ")
    if choice == "1":
        calculator()
    elif choice == "2":
        read_file()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")