# class and object:

print("-------------Example 1------------")
# creating class
class Student():
    name = "Karan Kumar"

# creating an object:
s1 = Student()
print(s1.name)


print("-------------Example 2------------")
class Car():
    brand = "BMW"
    color = "blue"

c1 = Car()
print(c1.color)
print(c1.brand)

print("-------------Example 3------------")
# when object is created, it points or invokes constructor in the class
# constructor calls for __init__():

class Student():
    # default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database...")

s1 = Student("Karan", 97)
print(s1.name, s1.marks)

s2 = Student("Sneha", 80)
print(s2.name, s2.marks)

"""Since only one constructor executes as parameters matches.
So default constructor will not execute. 
Therefore, we can go for only one constructor as shown below."""

print("-------------Example 4------------")
class Student():

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database...")

s1 = Student("Karishma", 99)
print(s1.name, s1.marks)

s2 = Student("Nandan", 87)
print(s2.name, s2.marks)

print("-------------Example 5------------")
# class attribute and object attribute:

class Student():

    college_name = "ABC college"    # class attr
    name = "Anonymous"  # class attr 

    def __init__(self, name, marks):
        self.name = name    # obj attr ---> preference always obj attr > class attr
        self.marks = marks  # obj attr
        print("Adding new student in Database...")

s1 = Student("Karishma", 99)
print(s1.name)
print(Student.college_name)
print(s1.college_name)

print("-------------Example 6------------")
# Attributes and Methods:

class Student():
    college_name = "ABC college"

    def __init__(self, name, marks):
        self.name = name     
        self.marks = marks  

    def welcome(self):
        print("Welcome student,", self.name)

    def get_marks(self):
        return "You have scored", self.marks

s1 = Student("Karishma", 99)
s1.welcome()
print(s1.get_marks())