print ("Welcome to my first calculator program nya")

class functions():
    def add(self, num1, num2):
        return (num1 + num2)
    def subtract(self, num1, num2):
        return (num1 - num2)
    def divide(self, num1, num2):
        return (num1 / num2)
    def multiply(self, num1, num2):
        return (num1 * num2)

calc = functions()

while True:

    num1 = float(input("Enter your first number nya: "))

    num2 = float(input("Enter your second number nya: "))

    function =  input("Would you like to add, subtract, divide, or multiply? ")

    if function == "add":
        result = calc.add(num1, num2)
        print(result)

    elif function == "subtract":
        result = calc.subtract(num1, num2)
        print(result)

    elif function == "divide":
        if num2 == 0:
            print("Sorry, try a different number.")
        else:
            result = calc.divide(num1, num2)
            print(result)

    elif function == "multiply":
        result = calc.multiply(num1, num2)
        print(result)

    else:
        print("Oops, try again!")

    again = input("Enter to continue calculations, quit to exit. ")
    if again.lower() == "quit":
        break