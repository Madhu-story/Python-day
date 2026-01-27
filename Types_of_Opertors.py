# Types of Opertaors are:

# 1. Arithmetic Operators:(+ , - , * , / , % , **)

a = 5
b = 2

print(a + b)  # add
print(a - b)  # difference
print(a * b)  # multiplication
print(a / b)  # division in decimal
print(a % b)  # gives us Remainder
print(a ** b)  # gives us power of, a^b

print("----------------------------------------------------------")

# 2. Relational Operators: (== , != , > , < , >= , <=): These gives us boolean values

print(a == b) 
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print("----------------------------------------------------------")

# 3. Assignment Operators: (= , += , -= , *= , /= , %=, **=)

num = 5

num += 2   # (num = num + 2) ------> (num = 5 + 2)
print("num is :", num)

num -= 2
print("num is :", num)

num *= 2
print("num is :", num)

num /= 2
print("num is :", num)

num %= 2
print("num is :", num)

num **= 2
print("num is :", num)

print("----------------------------------------------------------")

# 3. logical Operators: (not, and, or)

a = 50
b = 20

print(not False)
print(not (a > b))   # here (a>b) is True

val1 = True
val2 = False

print("AND Operator :", val1 and val2)   # both the values are checked, if both values are True, then only ans will be True

print("OR Operator :", (a == b) or (a > b))   # (a==b)--->False,  (a>b)--->True
print("OR Operator :", val1 or val2)  # If any one value is True, then ans will be True.

