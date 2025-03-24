"""generator"""

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
# gen=my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

"""decorator"""

# def my_decorator(func):
#     def wrapper():
#         print("function before")
#         func()
#         print("function after")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("hai")
# say_hello()

"""list element change"""
# list=[1,2,3,4,5]
# list[1]=553
# print(list)

# list_comp=[x**2 for x in range(5)]
# print(list_comp)

# dic_comp={x:x**2 for x in range(5)}
# print(dic_comp)

# set_comp={x**3 for x in range(5)}
# print(set_comp)

# add=lambda x,y:x+y
# print(add(5,5))

# square=lambda x:x**2
# print(square(4))

# maximum=lambda a,b:a if a > b else b
# print(maximum(10,20))

# numbers=[1,2,3,4,5]
# squared=list(map(lambda x:x**2 , numbers))
# print(squared)

# numbers=[1,2,3,4,5,6,7]
# filtered=list(filter(lambda x:x%2==0,numbers))
# print(filtered)

from functools import reduce

# numbers=[1,2,3,4,5,6,7]
# result=reduce(lambda x,y:x+y,numbers)
# print(result)

# numbers=[2,4,4]
# result=reduce(lambda x,y:x*y,numbers)
# print(result)


# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self,amount):
#         if amount >=0 :
#             self.__balance =amount
#         else:
#             print("balance cannot be negative")
#
# account=BankAccount("mahendra",80000)
#
# print(account.get_balance())
#
# account.set_balance(105000)
# print(account.get_balance())
#
# account.set_balance(-500)

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self,amount):
#         if amount >= 0:
#             self.__balance=amount
#         else:
#             print("balance cannot be negative")
#
# amount=BankAccount("mahendra",150000)
#
# print(amount.get_balance())
#
# amount.set_balance(200000)
# print(amount.get_balance())
#
# amount.set_balance(-5)


# class Car:
#
#     def __init__(self,model,price):
#         self.model=model
#         self.price=price
#
#     def display_details(self):
#         print(f"model:{self.model},price:{self.price}")
#
# car1=Car("toyota",1000000)
# car2=Car("hyundai",750000)
#
# car1.display_details()
# car2.display_details()

# dict={("car"):"luxury","price":150000}
# # dict["cost"]=dict.pop("price")
# # print(dict)
# dict["price"]=200000
# print(dict)


"""method overriding"""
# Parent class
# class Animal:
#     def speak(self):
#         print("animal sounds")
#
# class Dog(Animal):
#     def speak(self):
#         print("dog barks")
#
# class Cat(Animal):
#     def speak(self):
#         print("cat meows")
#
# animal=Animal()
# dog=Dog()
# cat=Cat()
#
# animal.speak()
# dog.speak()
# cat.speak()


# class Calculator:
#     # Method with default parameters
#     def add(self, a, b=0, c=0):
#         return a + b + c
#
# # Create an instance of Calculator
# calc = Calculator()
#
# # Calling the add method with different arguments
# print(calc.add(10))         # Output: 10 (10 + 0 + 0)
# print(calc.add(10, 20))     # Output: 30 (10 + 20 + 0)
# print(calc.add(10, 20, 30)) # Output: 60 (10 + 20 + 30)

# class Calculator:
#     # Method using *args to accept any number of arguments
#     def add(self, *args):
#         return sum(args)
#
# # Create an instance of Calculator
# calc = Calculator()
#
# # Calling the add method with different numbers of arguments
# print(calc.add(10))             # Output: 10
# print(calc.add(10, 20))         # Output: 30
# print(calc.add(10, 20, 30, 40)) # Output: 100


"""single inheritance"""
# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# # Creating an object of the subclass
# dog = Dog()
# dog.speak()  # Inherited method from Animal
# dog.bark()   # Method from Dog

"""multiple inheritance"""
# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog:
#     def bark(self):
#         print("Dog barks")
#
# class Labrador(Animal, Dog):
#     def description(self):
#         print("Labrador is a breed of dog.")
#
# # Creating an object of the subclass
# lab = Labrador()
# lab.speak()       # Inherited from Animal
# lab.bark()        # Inherited from Dog
# lab.description() # Method in Labrador class


# class Animal:
#     def speak(self):
#         print("Animal speaks")
#

"""multilevel """
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# class Puppy(Dog):
#     def cute(self):
#         print("Puppy is cute")
#
# # Creating an object of the subclass
# puppy = Puppy()
# puppy.speak()  # Inherited from Animal
# puppy.bark()   # Inherited from Dog
# puppy.cute()   # Method in Puppy class


"""hierarchial inheritance"""

# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")
#
# # Creating objects of the subclasses
# dog = Dog()
# cat = Cat()
#
# dog.speak()  # Inherited from Animal
# dog.bark()   # Method in Dog
# cat.speak()  # Inherited from Animal
# cat.meow()   # Method in Cat

"""hybrid inheritance"""

# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Mammal(Animal):
#     def walk(self):
#         print("Mammal walks")
#
# class Bird(Animal):
#     def fly(self):
#         print("Bird flies")
#
# class Bat(Mammal, Bird):
#     def hang(self):
#         print("Bat hangs upside down")
#
# # Creating an object of the subclass
# bat = Bat()
# bat.speak()  # Inherited from Animal
# bat.walk()   # Inherited from Mammal
# bat.fly()    # Inherited from Bird
# bat.hang()   # Method in Bat class

"""abstraction """

# from abc import ABC, abstractmethod
#
#
# # Abstract Class
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):  # Abstract method
#         pass
#
#     @abstractmethod
#     def move(self):  # Abstract method
#         pass
#
#
# # Subclass that inherits from Animal
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
#     def move(self):
#         print("Runs on four legs")


# Subclass that inherits from Animal
# class Bird(Animal):
#     def sound(self):
#         print("Chirp")
#
#     def move(self):
#         print("Flies in the sky")
#
#
# # Create instances of the subclasses
# dog = Dog()
# bird = Bird()
#
# dog.sound()  # Output: Bark
# dog.move()  # Output: Runs on four legs
#
# bird.sound()  # Output: Chirp
# bird.move()  # Output: Flies in the sky

##############
# Opening the file in write mode
# with open("example.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a simple file handling example.\n")
#
# print("Data written to file successfully.")
#
# import os
#
# # Print the current working directory
# print("Current working directory:", os.getcwd())
# ############
# # Opening the file in append mode
# with open("example.txt", "a") as file:
#     file.write("This is another line.\n")
#     file.write("Here's one more line added to the file.\n")
#
# print("Additional lines have been written to the file.")
# # ###########
# # Opening the file in append mode
# with open("example.txt", "a") as file:
#     for i in range(1, 11):  # Looping 10 times
#         file.write(f"This is line number {i}\n")  # Writing each line
#
# print("10 lines have been written to the file.")

#########################
# try:
#     # Trying to open a file that may not exist
#     with open("example.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Error: The file does not exist.")
# else:
#     print("File read successfully.")
# finally:
#     print("This block always executes, whether there is an error or not.")

######################
# try:
#     # Trying division by zero
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# else:
#     print("The operation was successful.")
# finally:
#     print("Execution complete.")


# def get_valid_quantity():
#     while True:
#         quantity=input("enter quantity(must be a positive integer):")
#         if quantity.isdigit() and int(quantity) >0:
#             print(f"valid quantity entered {quantity}")
#             break
#         else:
#             print("invalid input!please enter positive integer")
#
# get_valid_quantity()


