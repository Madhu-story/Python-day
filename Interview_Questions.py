# Practice problems (very important):
print("-------------Question 1------------------")
# Find largest & smallest number in a list (without max() / min())

nums = [34, 76, 23, 56, 12 , 87, 45, 96, 2]
# print("Maximum:", max(nums))
# print("Minimum:", min(nums))

i = 0
j = 1

while i <= len(nums)-2:
    while j <= len(nums)-1:
        if nums[i] > nums[j]:
            print(nums[i])
            # nums[j] == nums[i]
        else:
            print(nums[j], j)
        j += 1
    i += 1
print("Largest number is: ", nums)

print("-------------Question 2------------------")
# Remove duplicates from a list using:


print("-------------Question 3------------------")
# Remove duplicates from a list using:
# Using set


print("-------------Question 4------------------")
# Remove duplicates from a list using:
# without using set


print("-------------Question 5------------------")
# Count frequency of elements in a list using dictionary


print("-------------Question 6------------------")
# Merge two dictionaries


print("-------------Question 7------------------")
# Find common elements between two lists using set


print("-------------Question 8------------------")
# Reverse a list without using reverse() or slicing


# LOOPS RELATED QUESTIONS


# Print multiplication table of a number

# Count vowels in a string

# Find sum of numbers in a list

# Print only even numbers from a list

# Reverse a string using loop

# FUNCTIONS RELATED QUESTIONS

# Add two numbers

# Check even or odd

# Find square of a number

# Find maximum of two numbers

# Count vowels in a string

# Sum of elements in a list



# MINI PROJECTS / CHALLENGES:
# Create a small program using functions:

# Menu-driven calculator

# Student marks calculator

# Simple ATM simulation (deposit, withdraw, balance)