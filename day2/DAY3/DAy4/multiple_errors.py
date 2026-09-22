try:
    a = int (input("Enter a number"))
    b = int(input("Enter a divisor:"))
    result = a/b
    print(f"Result:{result}")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid number")
except Exception as e:
    print(f"Unexpected error:{e}")