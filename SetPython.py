collection = {1, 2, 2, 5, 8, "Hello", "world", "helllllooo", "world", 9, 3}

print(len(collection))
print(collection)

emp_set = set()
print(type(emp_set))

emp_set.add("Hello world")
emp_set.add(1)
emp_set.add(2)
emp_set.add(3)
emp_set.add(2)
emp_set.add((5, 4, 6))

print(len(emp_set))
print(emp_set)

emp_set.remove(2)

collect = {8, 4, 6, 234, 89.5, "ewedasd"}
print(collect)
collect.clear()
print(len(collect))

nums = {"hello", "apnacollege", "Madhura", "Python", "learning"}
print(nums)
nums.pop()
print(nums)

# UNION and INTERSECTION

set1 ={1, 2, 3, 5, 7, 9, 4, 6}
set2 = {3, 4, 5, 6, 7, 8, 9, 8}

print("Union of set: ", set1.union(set2))     # Union
print(set1)
print(set2)
print("Interscetion of set: ", set1.intersection(set2))    # Intersection
