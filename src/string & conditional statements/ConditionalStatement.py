print("--------------example-1------------")

light = "green"

if light == "red":
    print("Stop")
elif light == "green":
    print("Go")
elif light == "yellow":
    print("Look")
else:
    print("Light is broken")

print("End of Code")

print("------------example-2--------------")

age = 34

if age >= 18:
    print("Can Vote")
else:
    print("Cannot Vote")

print("------------example-3--------------")

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
else:
    grade = "D"

print("Grade  of the student is -->", grade)


# NEsting:

age = 87

if age >= 18:
    if age >= 80:
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")
