# About String: 

st1 = "Madhu"
st2 = 'Madhu'
st3 = """Madhu"""

# All these 3 types of writing strings are acceptable.

str1 = "Madhu"
len1 = len(str1)
print(len1)

str2 = "Stories"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))

print("----------------------------------------")

# Indexing:

str = "Madhu stories"
ch = str[4]
print(ch)

print("----------------------------------------")

# Slicing:

str = "Madhu Stories"
print(str[1:4])
print(str[:7])
print(str[3:])
print(str[2:len(str)])

# Negative indexing
print("---Negative index---")
str7 = 'Apple'
print(str7[-5])
print(str7[-3:-1])

print("----------------------------------------")

# String Functions:

str = "i am studying python from ApnaCollege."

print(str.endswith("ege."))
print(str.endswith("ege"))

print(str.capitalize())
# capitalize() only capitalizes the 1st char only when it is called else.
print(str)

# can't use capitalize() all the time. so,
print("---Capitalize()---")
str2 = "apna college is teaching python and also teaching Javascript."
str2 = str2.capitalize()
print(str2)

print("---replace()---")
print(str.replace("o", "a"))
print(str.replace("python", "Javascript"))

print("---find()---")
print(str.find("o"))
print(str2.find("is"))

print("---count()---")
print(str2.count("a"))
print(str2.count("teaching"))