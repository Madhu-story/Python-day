print("------------FUNCTIONS - example 30------------------")
# WAF to print the length of a list. (list is the parameter)

cities = ["Bengaluru", "Delhi", "Mumbai", "Goa", "Tamil Nadu", "Kerala", "Andhra Pradesh"]

def length(cities):
    print(len(cities))
    return len(cities)

length(cities)


print("------------FUNCTIONS - example 31------------------")
# WAF to print the elements of a list in a single line. (list is the parameter)

def elements(list):
    for i in list:
        print(i, end=", ")

elements(cities)


print("------------FUNCTIONS - example 32------------------")
# WAF to the factorial of n. (n is the parameter)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

factorial(4)


print("------------FUNCTIONS - example 33------------------")
# WAF to convert USD to INR

def conversion(usd_val):
    inr_val = usd_val * 90.39
    print(usd_val, "USD =", inr_val, "INR")

conversion(5)


print("------------FUNCTIONS - HOME WORK------------------")
# WAF to return the given number is EVEn or ODD.

def check(num):
    if num % 2 == 0:
        return "The given number is 'EVEN'"
    else:
        return "The given number is 'ODD'"
    
checking = check(77)
print(checking)


print("-----------Recursive FUNCTIONS - example 34------------------")
# Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if n == 0:
        return 0
    return (n + calc_sum(n-1))

print("Sum of natural numbers --> ",calc_sum(10))


print("-----------Recursive FUNCTIONS - example 35------------------")
# Write a recursive function to print all the elements in a list. [HINT: use list & index as parameters]

heroes = ["Ironman", "Superman", "Batman", "Ultraman", "Spiderman", "Antman", "Shaktiman"]

def elements(list, idx=0):
    if idx == len(list):
        return 0
    print(list[idx], end=", ")
    elements(list, idx+1)

elements(heroes)
