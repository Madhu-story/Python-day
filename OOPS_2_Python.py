# del keyword:

class Car:
    def __init__(self, brand):
        self.brand = brand

c1 = Car("Hyundai")
# print(c1.brand)

# del c1.brand
# # print(c1.brand)

# print(c1)
# del c1
# print(c1)

print()
print("------------------------------------")
# Private attributes and methods:
print("--------------Example 1----------------------")

class Account():

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        # self.acc_pass = acc_pass 
        self.__acc_pass = acc_pass    # TO make it "PRIVATE" add "__" (double underscore before the attribute)

    def reset(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
# # print(acc1.acc_pass)
# print(acc1.__acc_pass)

print("--------------Example 2----------------------")

class Person():
    __name = "Anonymous"

    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()
# p1.__hello()

print()
print("------------------------------------")
# Inheritance:
print("---------------Single Inheritance---------------------")
class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped....")

class ToyotaCar(Car):

    def __init__(self, name):
        self.name = name


c1 = ToyotaCar("Fortuner")
c2 = ToyotaCar("Etios")
print(c1.name, c1.color)
c1.start()


print("---------------Muti - Level Inheritance---------------------")

class Cars:
    color = "BLUE"

    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped....")

class HyundaiCars(Cars):

    def __init__(self, brand):
        self.brand = brand

class ModelCars(HyundaiCars):

    def __init__(self, type):
        self.type = type


c11 = ModelCars("Diesel")
c12 = HyundaiCars("Asta i20")

c11.start()
print(c12.brand)
print(c11.color)
print(c11.type)
c11.stop()

print("---------------Mutiple Inheritance---------------------")

class A:
    varA = "Welcome to variable class A"

class B:
    varB = "Welcome to variable class B"

class C(A, B):
    varC = "Welcome to variable class C"

o = C()
print(o.varC)
print(o.varB)
print(o.varA)


print("---------------Super Method---------------------")

class Cars:
    color = "BLUE"

    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped....")

class HyundaiCars(Cars):

    def __init__(self, brand):
        self.brand = brand

class ModelCars(HyundaiCars):

    def __init__(self, type, brand):
        super().__init__(brand)
        self.type = type

        super().start()
        super().stop()

c11 = ModelCars("Diesel", "Asta i20")
print(c11.type, c11.brand, c11.color)

print()
print("---------------class Method--------------------")
print("---------------Example 1--------------------")

# Class Metho:

class Person:
    name = "Anonymous"

    def changeName(self, name):
        self.name = name

per = Person()
per.changeName("Roshan")
print(per.name)
print(Person.name)

print("---------------Example 2--------------------")

class Person2:
    name = "Anonymous"

    def changeName(self, name):
        Person2.name = name

per = Person2()
per.changeName("Swathi")
print(per.name)
print(Person2.name)

print("---------------Example 3--------------------")

class Person3:
    name = "Anonymous"

    def changeName(self, name):
        self.__class__.name = name

per = Person3()
per.changeName("Ananya")
print(per.name)
print(Person3.name)

print("----------Class Method --- Example 4------------")

class Person4:
    name = "Anonymous"

    @classmethod
    def changeName(cls, name):  # cls ---> means class
        cls.name = name

per = Person4()
per.changeName("Chaitanya")
print(per.name)
print(Person4.name)

print()
print("---------------Property decorator--------------------")
# Property:

class Student:

    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(98, 94, 99)
print(s1.percentage)

s1.phy = 89
print("New percentage -->", s1.percentage)

print()
print("-------------------POLYMORPHISM-------------------")

# These are called implicit overloading, means automatically understands the type
# as "+" sign is acting according to the type of data
print(1 + 2)    # 3
print("My" + " World")  # concatenate
print([1, 2, 3] + [4, 5, 6])    # merge

print("------------POLYMORPHISM - Complex Number-------------")

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i", "+", self.img, "j")

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 8)
num2.showNumber()

print("------------Complex Number---Example 1----------")

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i", "+", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real     # here, self pointing to num1
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(2, 5)
num1.showNumber()

num2 = Complex(7, 6)
num2.showNumber()

print("-----------")
# num3 = num1 + num2        # TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'
num3 = num1.add(num2)       # So, we need to use .add function 
num3.showNumber()

print("-------Complex Number---Example 2--- Explicitly Overloading--------")

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i", "+", self.img, "j")

    def __add__(self, num2):        # just by giving dunder ("__") to add function
        newReal = self.real + num2.real     # here, self pointing to num1
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(7, 5)
num1.showNumber()

num2 = Complex(-2, 6)
num2.showNumber()

print("-----------")
num3 = num1 + num2       
#  We are explicitly overloading and informing that we need to add 2 complex numbers
num3.showNumber()

print("-------Complex Number---Example 3--- Explicitly Overloading--------")

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i", "-", self.img, "j")
    
    def __sub__(self, num2):        # just by giving dunder ("__") to add function
        newReal = self.real - num2.real     # here, self pointing to num1
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(7, 5)
num1.showNumber()

num2 = Complex(-2, 6)
num2.showNumber()

print("-----------")
num3 = num1 - num2       
#  We are explicitly overloading and informing that we need to add 2 complex numbers
num3.showNumber()