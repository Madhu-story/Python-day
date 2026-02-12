print("------tuple-------")
tup = (5, 6, 2, 1)
print(tup)
print(type(tup))

print("------Empty tuple-------")
tup1 = ()
print(tup1)
print(type(tup1))

print("------NOT tuple-------")
tup2 = (5)
print(tup2)
print(type(tup2))

print("------Single value tuple-------")
tup3 = (5,)
print(tup3)
print(type(tup3))

print("------add any elements with , or without , tuple-------")
tup4 = (5,6, 2, 6,5,)
print(tup4)
print(type(tup4))

print("------tuple Slicing-------")
print(tup[1:4])
print(tup[:4])
print(tup[1:])
print(tup[-3:-1])

print("------tuple Methods-------")
tuppy = (6, 2, 65, 132, 87, 123, 9, 1, 2, 6, 6, 6, 2, 2, 7, 1,)

print("------index(el)-------")
print(tuppy.index(123))

print("------count(el)-------")
print(tuppy.count(6))