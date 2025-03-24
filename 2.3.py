
"""example: sending messages"""
# employees=['raj','sita','mahesh','priya']
#
# for employee in employees:
#     print(f"hello {employee}, your salary has been credited")


# employees=['raj','sita','mahesh','priya']
# #
# employees.sort()
#
# print(employees)
#
# employees.reverse()
#
# print(employees)


# employees=['raj','sita','mahesh','priya']
#
# if 'sita' in employees:
#     print('sita ia an employee')
# else:
#     print('sit is not an employee')


"""list comprehension"""

# even_numbers=[x for x in range(1,11) if x%2==0]
# print(even_numbers)

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# num=int(input("enter a number"))
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num}is not a prime number")
#
#

"""5-2-2025"""

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# num=int(input("enter a number:"))
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
#

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**.5)+1):
#         if n%i==0:
#             return False
#     return True
# num=int(input("enter number:"))
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


"""reversed string"""
# string='apple'
# reversed_string=''
#
# for i in string:
#     reversed_string=i+reversed_string
# print(reversed_string)


# string='this is a car'
# strings=string.split()
# stringss=strings[3]
# print(stringss)


"""count letter a """
# string='where are you'
# print(string.count('a'))


"""replace key"""

# dict1={'school':'gowtham','place':'rajahmundry'}
# dict1['location']=dict1.pop('place')
# print(dict1)


"""largest and second largest strings"""
# strings=['sita','swetha','gayatri','gowri-shankar']
# longest_string=''
# second_largest_string=''
# for string in strings:
#     if len(string)>len(longest_string):
#         second_largest_string=longest_string
#         longest_string= string
#     elif len(string)>len(second_largest_string)and string!=longest_string:
#         second_largest_string=string
# print(longest_string)
# print(second_largest_string)


"""factorial number"""

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# num=5
# print(f'factorial of {num} is {factorial(num)}')

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# num=5
# print(f'factorial of {num} is {factorial(num)}')


"""palindrome check"""

# def is_palindrome(string):
#     return string==string[::-1]
#
# word=input("enter a word")
# if is_palindrome(word):
#     print(f"{word} is a palindome")
# else:
#     print(f"{word} is not a palindrome")

"""round a number to 2 decimal places"""

# num=12.34567
# rounded_num=round(num,2)
# print(rounded_num)


"""prime numbers"""

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# for num in range(1,51):
#     if is_prime(num):
#         print(num,end=" ")


"""list indexing"""
# fruits=['apple','banana','cherry','mango']
#
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

"""patterns"""

# for i in range(1,5):
#     print(' '*(5-i)+'*'*(2*i-1))

# for i in range(5,0,-1):
#     print(' '*(5-i)+'*'*(2*i-1))
#
#
# rows=5
# for i in range(rows-1,0,-1):
#     print(' '*(rows-i)+'*'*(2*i-1))
#     print(' '*(rows-1)+'*')


# rows=5

# for i in range(rows-1,0,-1):
#     print(' '*(rows-i)+"*"*(2*i-1))
#     print(' '*(rows-1)+'*')

# for i in range(6):
#     print('*'*i)
#
# for i in range(6,0,-1):
#     print('*'*i)

# for i in range(1,6):
#     print(str(i)*i)

# for i in range(6,0,-1):
#     print(str(i)*i)

# for i in range(1,6):
#     print(''.join(str(j)for j in range(1,i+1)))

# for i in range(6,0,-1):
#     print(''.join(str(j) for j in range(1,i+1)))

"""pyramid pattern with numbers"""

# for i in range(1,6):
#     print(' '*(5-i)+" " .join(str(j) for j in range(1,i+1)))


# for i in range(1,6):
#     print(' '*(5-i)+" ".join(str(j) for j in range(1,i+1)))

"""generator"""
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen=simple_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

"""decorator"""
# def my_decorator(func):
#     def wrapper():
#         print("before the function call")
#         func()
#         print("after the function call")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("hello,world")
#
# say_hello()

# def greet_decorator(func):
#     def wrapper(name):
#         print("welcome")
#         func(name)
#         print("have a nice day")
#     return wrapper
# @greet_decorator
# def greet(name):
#     print(f"hello,{name}")
#
# greet("manikanta")



"""class and object"""
# class Car:
#     def __init__(self,model,price):
#         self.model=model
#         self.price=price
#
#     def display_details(self):
#         print(f"model:{self.model},price:{self.price}")
#
# car1=Car("toyota",100000)
# car2=Car("maruti",200000)
#
# car1.display_details()
# car2.display_details()


# class BankAccount:
#     def __init__(self,holder,balance):
#         self.holder=holder
#         self.__balance=balance
#
#     def deposit(self,amount):
#         if amount >0:
#             self.__balance+=amount
#
#     def withdraw(self,amount):
#         if amount <=self.__balance:
#             self.__balance-=amount
#
#         else:
#             print("insufficient funds")
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self,balance):
#         if balance>=0:
#             self.__balance=balance
#         print("balance cannot be negative")
#
# account=BankAccount("Manikanta",5000)
# account.deposit(2000)
# account.withdraw(1000)
# print(account.get_balance())
# account.set_balance(7000)
# print(account.get_balance())

"""polymorphism----method overriding"""

# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
#
# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")
#
# animal=Animal()
# dog=Dog()
# cat=Cat()
#
# animal.speak()
# dog.speak()
# cat.speak()

"""polymorphism ----overloading"""

# class Calculator:
#     def add(self,*args):
#         return sum(args)
#
# calc=Calculator()
# print(calc.add(5))
# print(calc.add(5,10))
# print(calc.add(5,10,15))


"""single---inheritance """

# class Animal:
#     def __init__(self,name):
#         self.name=name
#
#     def speak(self):
#         print(f"{self.name} makes a sound")
#
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks")
#
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} meows")
#
# dog=Dog("Buddy")
# cat=Cat("Whiskers")
#
# dog.speak()
# cat.speak()



# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**.5)+1):
#         if n%i==0:
#             return False
#     else:
#         return True
# num=int(input("enter number:"))
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f'{num} is not a prime number')


"""single inheritance"""

# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# #create object of Dog
# dog=Dog()
#
# dog.speak()
# dog.bark()

"""multiple inheritance"""

# base class 1
# class Animal:
#     def speak(self):
#         print("animal speaks")
# base class 2
# class Pet:
#     def love(self):
#         print("pet  loves you")
#
# # Derived class
# class Dog(Animal,Pet):
#     def bark(self):
#         print("Dog barks")
#
# # create object of dog
# dog=Dog()
#
# dog.speak()
# dog.love()
# dog.bark()

"""multilevel inheritance"""

# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# class Puppy(Dog):
#     def play(self):
#         print("puppy plays")
#
# puppy=Puppy()
#
# puppy.speak()
# puppy.bark()
# puppy.play()

"""7-2-2025"""

# numbers=[1,2,3,4]
# result=set(map(lambda x:x**2,numbers))
# print(result)

# Generator expression
# gen = (x * 2 for x in range(5))
#
# # Iterating over the generator
# for value in gen:
#     print(value)

# Generator expression
# gennnn = (x * 2 for x in range(5))
#
# # Iterating over the generator
# print(next(gennnn))  # Output: 0
# print(next(gennnn))  # Output: 2
# print(next(gennnn))  # Output: 4
# print(next(gennnn))
# print(next(gennnn))
# print(next(gennnn))

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()
#
# # The values are generated on the fly when you iterate over them
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))




# def simple_decorator(func):
#     def wrapper():
#         print("before going")
#         func()
#         print("after going")
#     return wrapper
# @simple_decorator
# def say_hello():
#
#     print("hai")
# say_hello()

# list_comp=[x*2  for x in range(5)]
# print(list_comp)
#
# dict_comp={x:x**2 for x in range(5)}
# print(dict_comp)
#
# set_comp={x-2 for x in range(7)}
# print(set_comp)


# def decorator_with_args_kwargs(func):
#     def wrapper(*args,**kwargs):
#         print("arguments passed to the the function")
#         print(f"positional arguments:{args}")
#         print(f"keyword arguments:{kwargs}")
#
#         result=func(*args,**kwargs)
#         return result
#     return wrapper
#
# @decorator_with_args_kwargs
# def greet(name,age=25):
#     print(f"hello {name},you are{age} years old")
# greet("alice",age=30)
# greet("bob")


# def print_number(*args):
#     for number in args:
#         print(number)
# print_number(1,2,3,4,5)

# def print_student_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# print_student_info(name="alice",age=25,grade="A")

# def sum_numbers(*args):
#     total=sum(args)
#     print(f"the sum is :{total}")
# sum_numbers(1,2,3,4,5,6,7)
# sum_numbers(1,2,3,4)

# def sum_numbers(*args):
#     total=sum(args)

#     print(f"the sum is {total}")
# sum_numbers(1,2,3,4)
# sum_numbers(1,2,3,4,5,6,7,8)

