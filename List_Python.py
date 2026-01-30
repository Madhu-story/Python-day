marks = [76, 98, 43, 26, 87, 56, 93]
student = ["Karan", 97, 16, "Delhi"]

print(student)
student[0] = "Arjun"
print(student)
print("length of student list is -->", len(student))


print("--------List Slicing--------")
# List Slicing which is similar to String Slicing

print(marks[1:4])
print(marks[:5])
print(marks[1:])
print(marks[-4:-1])

print("--------List Methods--------")
list = [5, 2, 7, 5, 9, 1, 5, 7, 3]
print(list)

print("--------append()--------")
list.append(17)
print(list)

print("--------sort()--------")
list.sort()
print(list)

print("--------sort(reverse=True)--------")
list.sort(reverse=True)
print(list)

# print("--------reverse()--------")
# list = list.reverse()
# print(list)

print("--------insert()--------")
list.insert(2, 14)
print(list)

print("--------remove()--------")
list.remove(5)
print(list)

print("--------pop()--------")
list.pop(4)
print(list)