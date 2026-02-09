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
