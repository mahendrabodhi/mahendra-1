


"""polymorphism"""

"""method overloading"""

# class Calculator:
#     def add(self,a,b=0,c=0):
#         return a+b+c
#
# calc=Calculator()
#
# print(calc.add(5,10))
# print(calc.add(10,100,1000))

"""method overloading  2"""
# class Calculator:
#     def add(self,*args):
#         return sum(args)
#
# calc=Calculator()
# print(calc.add(10,20,50,100))
# print(calc.add(100,1000,2000))


"""method overloading with @static method"""

# class MathOperations:
#     @staticmethod
#     def multiply(a,b=None):
#         if b is not None:
#             return a*b
#         return  a*a
#
# print(MathOperations.multiply(5))
# print(MathOperations.multiply(10,5))


"""public encapsulation"""

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def show_details(self):
#         print(f"Employee:{self.name},salary:{self.salary}")
#
# emp=Employee("Rakesh",45000)
# print(emp.name)
# print(emp.salary)
# emp.show_details()

"""protected encapsulation"""


# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self._balance=balance
#
#     def show_balance(self):
#         print(f"Account owner:{self.owner},balance:{self._balance}")
# class SavingsAccount(BankAccount):
#     def access_balance(self):
#         print(f"Accessing balance inside subclass:{self._balance}")
#
# acc=SavingsAccount("Manikanta",100000)
# print(acc.owner)
# print(acc._balance)
# acc.access_balance()


# class Customer:
#     def __init__(self,name,account_pin):
#         self.name=name
#         self.__account_pin=account_pin
#
#     def get_pin(self):
#         return self.__account_pin
#
# cust=Customer("Mahendra",1234)
# print(cust.name)
# print(cust.get_pin())


# class Animal:
#     def __init__(self,type,colour):
#         self.type=type
#         self.colour=colour
#
#     def show(self):
#         print(f"Animal details:{self.type},colour:{self.colour}")
#
# animal=Animal("cow","white")
# animal.show()





# class parent:
#     def big(self):
#         print("hai")
#
# class child(parent):
#     def small(self):
#         print("hello")
#
# c=child()
# c.small()
# c.big()


# class Father:  # ✅ First Parent Class
#     def father_details(self):
#         print("Father: Rajesh")
#
# class Mother:  # ✅ Second Parent Class
#     def mother_details(self):
#         print("Mother: Sita")
#
# # ✅ Child class inheriting from both Father and Mother
# class Child(Father, Mother):
#     def child_details(self):
#         print("Child: Manikanta")
#
# # ✅ Creating an object of Child class
# c = Child()
#
# # ✅ Calling methods from both parent classes and child class
# c.child_details()   # Output: Child: Manikanta
# c.father_details()  # Output: Father: Rajesh  (Inherited from Father)
# c.mother_details()  # Output: Mother: Sita  (Inherited from Mother)


# class Parent:
#     def show(self):
#         print("this is the parent class")
#
# class Child(Parent):
#     def display(self):
#         print("this is the child class")
#
# obj=Child()
#
# obj.show()
# obj.display()

# class Parent:
#     def show(self):
#         print("This is the Parent class")
#
# class Child(Parent):
#     def __init__(self):
#         print("Child class constructor")
#         self.show()  # Calling parent class method inside constructor
#
# obj = Child()  # Instantiating child class

# class Parent:
#     def show(self):
#         print("This is the Parent class")
#
# class Child(Parent):
#     def display(self):
#         print("This is the Child class")
#         super().show()  # Calling parent class method using super()
#
# obj = Child()
# obj.display()  # First, child class method executes, then parent class method is called
#

# class Parent:
#     def show(self):
#         print("This is the Parent class")
#
# class Child(Parent):
#     def show(self):  # Overriding the parent method
#         print("This is the Child class overriding Parent class")
#
# obj = Child()
# obj.show()  # Calls the overridden method in Child class

# class Father:
#     def father_info(self):
#         print("Father's information")
#
# class Mother:
#     def mother_info(self):
#         print("Mother's information")
#
# class Child(Father, Mother):  # Inheriting from both Father and Mother
#     def child_info(self):
#         print("Child's information")
#
# obj = Child()
# obj.father_info()
# obj.mother_info()
# obj.child_info()
#
# class Parent:
#     def show(self):
#         print("Parent class method")
#
# class Child1(Parent):
#     def display1(self):
#         print("Child1 class method")
#
# class Child2(Parent):
#     def display2(self):
#         print("Child2 class method")
#
# obj1 = Child1()
# obj1.show()   # Accessing Parent class method
# obj1.display1()
# obj2 = Child2()
# obj2.show()   # Accessing Parent class method
#
#
# class Parent:
#     def show(self):
#         print("this is the parent class")
#
# class Child(Parent):
#     def display(self):
#         print("thia is child class")
#
# obj=Child()
# obj.display()
# obj.show()
"""multiple inheritance"""
# class Father:
#     def father_info(self):
#         print("father information")
#
# class Mother:
#     def mother_info(self):
#         print("mother information")
#
# class Child(Father,Mother):
#     def child_info(self):
#         print("child information")
#
# obj=Child()
# obj.child_info()
# obj.father_info()
# obj.mother_info()

"""multilevel inheritance"""
# class Grandfather:
#     def method1(self):
#         print("method from grandfather")
#
# class Father(Grandfather):
#     def method2(self):
#         print("method from father")
#
# class Child(Father):
#     def method3(self):
#         print("method from child")
#
# obj=Child()
# obj.method1()
# obj.method2()
# obj.method3()

"""hierarchical inheritance"""
# class Parent:
#     def show(self):
#         print("method from parent")
#
# class Child1(Parent):
#     def method1(self):
#         print("method from child1")
# class Child2(Parent):
#     def method2(self):
#         print("method from child2")
#
# obj1=Child1()
# obj2=Child2()
#
# obj1.method1()
# obj1.show()
#
# obj2.method2()
# obj2.method2()

"""hybrid inheritance"""
# class A:
#     def methodA(self):
#         print("method from A")
#
# class B(A):
#     def methodB(self):
#         print("method from B")
#
# class C(A):
#     def methodC(self):
#         print("method from C")
#
# class D(B,C):
#     def methodD(self):
#         print("method from D")
#
# obj=D()
#
# obj.methodA()
# obj.methodB()
# obj.methodC()
# obj.methodD()



# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#
#     def fuel_type(self):
#         print("fuel type:petro/diesel")
#
# class Car(Vehicle):
#     def start(self):
#         print("car starts with key")
#
# class Bike(Vehicle):
#     def start(self):
#         print("bike starts with button")
#
# car=Car()
# car.start()
# car.fuel_type()
#
# bike=Bike()
# bike.start()
# bike.fuel_type()


# from abc import ABC,abstractmethod
#
# class Bank(ABC):
#     @abstractmethod
#     def loan_interest(self):
#         pass
#
#     def amount(self):
#         print("amount in account:1000000")
# class SBI(Bank):
#     def loan_interest(self):
#         print("SBI loan interest rate:8.5%")
#
# class HDFC(Bank):
#     def loan_interest(self):
#         print("HDFC loan interest rate:9.0%")
#
# sbi=SBI()
# sbi.loan_interest()
# sbi.amount()
#
# hdfc=HDFC()
# hdfc.loan_interest()
# hdfc.amount()
#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass  # No implementation in the abstract class
#
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
#
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
#
# dog = Dog()
# print(dog.sound())  # Output: Bark
#
# cat = Cat()
# print(cat.sound())  # Output: Meow

# from abc import ABC, abstractmethod
#
# # Abstract Class (Base Class)
# class Shape(ABC):
#     @abstractmethod
#     def area(self):  # Abstract method (no implementation)
#         pass
#
#     def describe(self):  # Concrete method
#         print("This is a shape")
#
# # Derived Class: Square (Inheriting from Shape)
# class Square(Shape):
#     def area(self):
#         self.describe()  # Calling the concrete method from Shape
#         return "Area = side x side"
#
# # Creating an object of Square class
# square = Square()
# print(square.area())


# from abc import ABC,abstractmethod
#
# class ATM(ABC):
#     @abstractmethod
#     def withdraw(self,amount):
#         pass
#
#     @abstractmethod
#     def deposit(self,amount):
#         pass
#
#     def check_balance(self):
#         print("Fetching balance....")
#
# class BankAccount(ATM):
#     def __init__(self,balance):
#         self.balance=balance
#
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             return f"withdraw:{amount},Remaining Balance:{self.balance}"
#         else:
#             "insufficient funds"
#
#     def deposit(self,amount):
#             self.balance+=amount
#             return f"deposited:{amount},new balance:{self.balance}"
#
# account=BankAccount(5000)
# print(account.deposit(2000))
# print(account.withdraw(3000))
# account.check_balance()

"""for loop"""

# emails=["hai@gmail.com","hello@gmail.com","helloworld@gmail.com"]
#
# for email in emails:
#     print(f"sending email to {email}...")
#
#     print("✅ email sent successfully")

"""for loops"""
# sales_transactions=[150.75,200.50,99.99,250.00,300.25]
#
# total_sales=0
# for sale in sales_transactions:
#     total_sales+=sale
#
# print(f"total sales:${total_sales:.2f}")



# inventory={"mouse":12,"laptop":8,"phone":15,"tablet":5,"macbook":5}
#
# for product,value in inventory.items():
#     if value <10:
#         print(f"{product} :stock is less")
#     else:
#         print(f"{product} :stock is sufficient")


# inventory={"mouse":10,"laptop":5,"tablet":3,"phone":12}
# item=input("enter product name: ").lower()
#
# if item in inventory:
#     print(f"{item.upper()} stock :{inventory[item]}")
# else:
#     print("item not found")
#
# inventory = {
#     "Electronics": {"Laptop": 10, "Phone": 5},
#     "Clothing": {"Shirt": 20, "Shoes": 15},
#     "Groceries": {"Rice": 50, "Sugar": 30}
# }
#
# for category, products in inventory.items():
#     print(f" {category}:")
#     for product, stock in products.items():
#         print(f"{product}: {stock} left")

# signal = input("Enter traffic signal color (Red/Yellow/Green): ").lower()
#
# if signal == "red":
#     print("Stop!")
# elif signal == "yellow":
#     print("Get Ready!")
# elif signal == "green":
#     print("Go!")
#     print("Invalid input!")
# else:
#     pass

