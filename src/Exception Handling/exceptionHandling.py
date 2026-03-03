
print("Resource opened Successfully.")

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError as zde:
    print("An error occurred: Division by Zero is not allowed", zde)
except ValueError as ve:
    print("An error occurred: Invalid input", ve)
except Exception as e:
    print("An unexpected error occurred", e)

finally:
    print("Resource Closed.")
