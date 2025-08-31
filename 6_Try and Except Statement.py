try:
  number = int(input("Enter a number: "))
  result = 10 / number
  print("The result is:", result)
except ZeroDivisionError:
  print("Division by zero is not allowed.")
except ValueError:
  print("Invalid input. Please enter a valid number.")
