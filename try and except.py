
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("Invalid input")

