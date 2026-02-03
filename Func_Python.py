# Learning FUNCTION IN PYTHON:

# Print Hello:
def print_hello():
    print("Hello")

# Add 2 numbers and return the output
def calc_sum(a, b):
    sum = a + b
    return "Sum: ",sum

# function calling
print_hello()
add = calc_sum(12, 81)
print(add)

# average of 3 numbers:
def calc_avg(a, b, c):
    avg = (a + b + c)/3
    return "Avg: ",avg

average = calc_avg(4, 17, 2)
print(average)


# Recursive functions:

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    print("END")

show(5)

# Example 2

def fact(n):
    if (n == 0 or n == 1):
        return 1
    return n * fact(n-1)

factorial = fact(6)
print(factorial)