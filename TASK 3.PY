#simple calculator task 3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def main():
    print("Welcome to Simple Calculator by pranav awari...!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation!")
                continue

            print("Result:", result)
            
            choice = input("Do you want to perform another calculation? (yes/no): ")
            if choice.lower() != 'yes':
                break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
