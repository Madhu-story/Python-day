# While loop:

i = 1
while i <=5:
    print("hello", i)
    i += 1

print("Loop Ended")

print("-------break--------")
# BREAK - Keyword in while loop

i = 0
while i <=5:
    if i == 3:
        break
    print(i)
    i += 1

print("-------continue--------")
# CONTINUE - Keyword in while loop

i = 0
while i <=5:
    if i == 3:
        i += 1
        continue    #Skips a count
    print(i)
    i += 1

print("--------example- continue------")
# One more example:

i = 0
while i <=5:
    if i % 2 == 0:
        i += 1
        continue# Here we het only odd numbers
    print(i)
    i += 1

print("--------FOR LOOP------")
print("--------example 1------")
# FOR LOOP

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in list:
    print(val)

print("-------FOR LOOP - example 2------")
veggies = ["onion", "tomato", "potato", "carrot", "brinjal", "drumstick"]
for veg in veggies:
    print(veg)

print("-------FOR LOOP - example 3------")
tup = (10, 9, 8, 7, 6, 5, 4, 3, 2)
for val in tup:
    print(val)
else:
    print("END")

print("-------FOR LOOP - example 4------")
str = "apnacollege"
for char in str:
    if char == "o":
        print("Found character", char)
        break
    print(char)
else:
    print("Not Found")

print("END")


print("--------RANGE()------")
print("--------example 1------")

for i in range(5):
    print(i)

print("-------RANGE() - example 2------")

for i in range(1, 5):
    print(i)


print("-------RANGE() - example 3------")

for i in range(2, 10, 2):
    print(i)

