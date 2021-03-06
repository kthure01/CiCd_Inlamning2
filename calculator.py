# Detta är en enkel app med några funktioner för att
# kunna visa en implementation av ett testförfarande
#

def addition(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "invalid"

    return x / y


def power(x, y):
    return pow(x, y)


def run_calc():
    run_app = True
    while run_app:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            operator = input("Enter operator [+,-,*,/,**]: ")
        except KeyboardInterrupt:
            print('An exception occurred\n\n')
            run_app = False
            break
        except ValueError:
            print('Invalid input\n\n')
            continue

        if operator == "+":
            print(num1, operator, num2, " = ", addition(num1, num2))
        elif operator == "-":
            print(num1, operator, num2, " = ", subtract(num1, num2))
        elif operator == "*":
            print(num1, operator, num2, " = ", multiply(num1, num2))
        elif operator == "/":
            print(num1, operator, num2, " = ", divide(num1, num2))
        elif operator == "**":
            print(num1, operator, num2, " = ", power(num1, num2))
        else:
            print("Wrong operator\n")

        tmp = input("Type Q to exit: ")
        print("\n")
        if tmp in ["Q", "q"]:
            run_app = False


if __name__ == "__main__":
    run_calc()
