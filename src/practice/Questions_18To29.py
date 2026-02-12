print("-----------------question 18---------------------")
# 18. Print numbers from 1 to 100

i = 1
while i <= 100:
    print(i)
    i += 1

print("-----------------question 19---------------------")
# 19. Print numbers from 100 to 1

i = 100
while i >= 1:
    print(i)
    i -= 1

print("-----------------question 20---------------------")
# 20. Print the multiplication table of number n.

i = 1
n = 2
while i <= 10:
    table = n * i
    print(n, "*", i, "=", table)
    i += 1 

print("-----------------question 21---------------------")
# 21. Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

print("-----------------question 22---------------------")
# 22. Search a number X in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 81
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index ",i)
    else:
        print("Finding....")
    i += 1


print("-----------------question 23---------------------")
# 23. Print the elements of the following list using a "FOR" loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list_value = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in list_value:
    print(val)

print("-----------------question 24---------------------")
# 22. Search a number X in this tuple using "FOR" loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup_values = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 64
idx = 0
for val in tup_values:
   if val == x:
      print("Found at index", idx)
      break
   print(val)
   idx += 1


print("-----------------question 25---------------------")
# Print number from 1 to 100.

for i in range(1, 101):
    print(i)


print("-----------------question 26---------------------")
# Print number from 100 to 1.

for i in range(100, 0, -1):
    print(i)

print("-----------------question 27---------------------")
# Print the multiplication table of a number n.

n = 4
# or  
# n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", (n*i))


print("-----------------question 28---------------------")
# WAP to find the sum of first n numbers (USING WHILE LOOP).

n = 10
# n = int(input("Enter the number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of the numbers -->", sum)


print("-----------------question 29---------------------")
# WAP to find the factorial of first n numbers (USING FOR LOOP).

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i 
print("Factorial of ",n, "is", fact)

