print("-----------OOPS - example 41------------------")
# Create a student class that takes name and marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.

class Student():

    def __init__(self, name, phy_mark, chem_mark, math_mark):
        self.name = name
        self.phy_mark = phy_mark
        self.chem_mark = chem_mark
        self.math_mark = math_mark

    def average(self):
        avg = (self.phy_mark + self.chem_mark + self.math_mark) / 3
        print("Welcome,", self.name)
        print("Your average score of 3 subjects -->", avg)

s1 = Student("Nalini", 98, 87, 95)
s1.average()

print("-----------OR take list------------------")

class Student():

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum/3
        
        print("Welcome,", self.name)
        print("Your average score of 3 subjects -->", avg)

s1 = Student("Nalini", [98, 87, 95])
s1.get_avg()

print("-----------OOPS - example 42------------------")
# Create Account class with 2 attributes - balance & account no. 
# Then create a method for debit, credit & printing the balance.

class Account():

    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, " got debited.")
        self.get_balance()
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, " got credited.")
        self.get_balance()

    def get_balance(self):
        print("Your current balance is Rs.",self.balance)

acc1 = Account(10000, 12345)
acc1.debit(2000)

acc1.credit(5000)


print("-----------OOPS - example 43------------------")
# Define a Circle class to create a circle with radius r using the constructor. 
# Define the Area() method of the class which calculates the area of the circle.
# Define the Permieter() method of the circle to calculate the perimeter.
from math import *

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = pi * (self.radius ** 2)
        a = '{:.2f}'.format(a)
        print("Area of the circle: ", a, "m")

    def perimeter(self):
        p = 2 * pi * self.radius
        p = '{:.2f}'.format(p)
        print("Perimeter of the circle: ", p, "m")
        

c = Circle(4)
c.area()
c.perimeter()

print("-----------OOPS - example 44------------------")
# Define a Employee class with attributes role, department & salary. 
# This class also showDetails()method.
# Create an Engineer class that inherits properties from Employee & has assitional att: name & age.

class Employee:

    def __init__(self, role, dep, sal):
        self.role = role
        self.dep = dep
        self.sal = sal

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.dep)
        print("Salary: Rp.",self.sal)


class Engineer(Employee):

    def __init__(self, name, age):
        super().__init__("Accountant", "Finance", "66,000")
        self.name = name
        self.age = age
        print("Name:", self.name)
        print("Age:", self.age)
        
        # self.showDetails()
        
e = Engineer("Dhanya", 27)
e.showDetails()


print("-----------OOPS - example 45------------------")
# Create a class called Order which stores item and price.
# Use dander function __gt__() to convey that:
# order 1 > order 2 if price of order 1 > price of order 2

class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("milk", 48)
order2 = Order("chips", 20)

print(order1 > order2)
