"""2nd largest string sorting function"""

#
# strings=['one','two','three','four','five','six','thirteen']
# largest=''
# second_largest=''
#
# for string in strings:
#     if len(string)>len(largest):
#         second_largest=largest
#         largest=string
#     elif len(string)>len(second_largest) and string!=largest:
#         second_largest=string
# print(largest)
# print(second_largest)


"""max value in the list"""
# numbers=[1,2,3,4,5,6,7]
#
# largest=numbers[0]
#
# for number in numbers:
#     if number>largest:
#         largest=number
# print(largest)

# s=['abcdf','abc','ab','a']
# print(sorted(s,key=len)[-2])


# s=[[10,1],[4,2],[3,12],[8,0]]
# print(sorted(s,key=sum))


"""remove duplicates"""

# list=[1,2,3,4,4,5,6,6,7,8,8,9,9]
#
# after_remove_duplicates=[]
# for i in list:
#     if  i not in after_remove_duplicates:
#       after_remove_duplicates.append(i)
# print(after_remove_duplicates)



"""replace key"""
# my_dict1={'school':'gowtham','place':'rajahmundry'}
# my_dict1['location']=my_dict1.pop('place')
# print(my_dict1)

"""prime members"""

# limit=100
#
# for j in range(2,limit+1):
#     is_prime=True
#     for i in range(2,int(j**.5)+1):
#         if j%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(j)


# squares={x:x**2 for x in range(5)}
# print(squares)

# lists=[1,2,3,4,5,6,7]
# add=list(map(lambda x:x+5,lists))
# print(add)


# for i in range(1,6):
#     print('*'*i)
#
# for i in range(5,0,-1):
#     print('*'*i)

"""right angle triangle with alphabets"""

# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end='')
#     print()

# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


"""fizz buzz"""

# n=20
#
# for i in range(1,n+1):
#     if i%3 ==0 and i%5==0:
#         print('fizzbuzz')
#     elif i%3==0:
#         print('fizz')
#     elif i%5==0:
#         print('buzz')
#     else:
#         print(i)

# for i in range(10):
#     if i%2==0:
#         print(i)


# def is_palindrome(string):
#     string=''.join(filter(str.isalnum,string)).lower()
#     return string==string[::-1]
#
# word="madam"
# print(is_palindrome(word))
#
# phrase="a man ,a plan,a canal,panama!"
#
# print(is_palindrome(phrase))

"""delete duplicates"""

# l=[0,1,2,4,4,5,5,6,6,7,8,9,9]
# dd=[]
#
# for i in l:
#     if i not in dd:
#         dd.append(i)
# print(dd)


"""pattern"""

# rows=6
# for i in range(1,rows):
#     print("*"*i)

# for i in range(5,0,-1):
#     print('*'*i)

# rows=5
# for i in range(1,rows):
#     print(' '*(rows-i)+'*'*(2*i-1))

# rows=5
# for i in range(rows-1,0,-1):
#     print(' '*(rows-i)+'*'*(2*i-1))
#     print(' '*(rows-1)+'*')

# rows=5
# for i in range(1,rows):
#     print(' '*(rows-i)+'*'*(2*i-1))
#     print(' '*(rows-1)+'*')


"""armstrong number---153,370,371,9474"""
#
# armstrong_number=153
#
# digits=str(armstrong_number)
# n=len(digits)
# total=0
#
# for digit in digits:
#     total+=int(digit)**n
# if total==armstrong_number:
#     print("number is armstrong_number")
# else:
#     print("number is not armstrong_number")


# armstrong_number=153
# digits=str(armstrong_number)
# n=len(digits)
# total=0
#
# for digit in digits:
#     total+=int(digit)**n
# if total==armstrong_number:
#     print("number is armstrong_number")
# else:
#     print("number is not armstrong_number")

# start,end=10,50
#
# for num in range(start,end+1):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print("prime:",num)

"""fibonacci sequence"""

# limit=10
# a,b=0,1
# print("fibonacci sequence")

# for i in range(limit):
#     print(a)
#     a,b=b,a+b



"""list methods"""
""" append """

# products=['laptop','smartphone','headphones']
# products.append('smartwatch')
# print(products)

"""extend"""

# products=['laptop','smartphone']
# new_products=['tablet','monitor']
# products.extend(new_products)
# print(products)

"""insert"""

# products=['laptop','smartphone','tablet']
# products.insert(0,'gaming console')
# print(products)


"""remove"""
# products=['laptop','smartphone','tablet']
# products.remove('tablet')
# print(products)

"""pop"""
# cart=['laptop','smartphone','tablet']
# last_item=cart.pop()
# print(last_item)
# print(cart)

"""index"""
# products=['laptop','smartphone','tablet']
# position=products.index("smartphone")
# print(position)

"""count"""
# cart=['laptop','laptop','smartphone','tablet']
# laptop_count=cart.count('laptop')
# print(laptop_count)

"""sort"""

# products=['smartphone','tablet','laptop']
# products.sort()
# print(products)

# prices=[299.99,799.99,499.99]
# prices.sort()
# print(prices)

"""reverse"""
# products=['laptop','smartphone','tablet']
# products.reverse()
# print(products)

"""copy"""
# products=['laptop','smartphone','tablet']
# backup=products.copy()
# print(backup)

"""clear"""

# cart=['laptop','smartphone','tablet']
# cart.clear()
# print(cart)

"""len"""
# products=['laptop','smartphone','tablet']
# print(len(products))

"""list comprehension"""
# prices=[299.99,399.99,799.99]
# affordable_products=[price for price in prices if price <500]
# print(affordable_products)



'''28/01/2025'''

"""class and object"""

"""class and object"""
# class Car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#
#     def display_details(self):
#         print(f'Brand:{self.brand},Model:{self.model},Price:{self.price}')
# car1=Car("toyota",'corolla',20000)
# car2=Car("honda",'civic',22000)
#
# car1.display_details()
# car2.display_details()


# class car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#
#     def display_details(self):
#         print(f"brand:{self.brand},model:{self.model},price:{self.price}")
#
# car1=car("toyota","corolla",20000)
# car2=car('honda','civic',22000)
#
# car1.display_details()
# car2.display_details()


"""encapsulation"""
#
# class bankaccount:
#     def __init__(self,account_number,balance):
#         self.__account_number=account_number
#         self.__balance=balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self,new_balance):
#         if new_balance>=0:
#             self.__balance=new_balance
#         else:
#             print("balance cannot be negative")
#
# account=bankaccount(123456,1000)
# account.set_balance(2000)
# print("updated balance:",account.get_balance())
# account.set_balance(-500)


"""inheritance"""
# class Vehicle:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     def display(self):
#         print(f"Vehicle Name: {self.name}, Speed: {self.speed} km/h")
#
# class Car(Vehicle):
#     def __init__(self, name, speed, fuel_type):
#         super().__init__(name, speed)
#         self.fuel_type = fuel_type
#
#     def display(self):
#         super().display()
#         print(f"Fuel Type: {self.fuel_type}")
#
# # Using inheritance
# car = Car("Honda Civic", 180, "Petrol")
# car.display()
#

"""polymorphism"""
# class Animal:
#     def sound(self):
#         print("Animals make sounds")
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
#
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
#
# # Using polymorphism
# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.sound()
#

"""abstraction"""

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
# # Using abstraction
# circle = Circle(5)
# print("Area of Circle:", circle.area())
#
#
#
#
# class Battery:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
# class Laptop:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery

# Composition example
# battery = Battery("5000mAh")
# laptop = Laptop("Dell", battery)
# print(f"Laptop Brand: {laptop.brand}, Battery Capacity: {laptop.battery.capacity}")



"""multiple inheritance"""
# class Teacher:
#     def teach(self):
#         print("Teaching students")
#
# class Researcher:
#     def research(self):
#         print("Conducting research")
#
# class Professor(Teacher, Researcher):
#     pass
#
# # Using multiple inheritance
# prof = Professor()
# prof.teach()
# prof.research()
#
#

"""operator overloading"""

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"
#
# # Operator overloading
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2
# print(v3)  # Output: Vector(6, 8)


# squares=(lambda x:x**2)
# print(squares(5))


"""2.9/01/2025"""
#
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self):
#         return self.__age
#
#     def set_age(self,new_age):
#         if new_age > 0:
#             self.__age=new_age
#         else:
#             print("invalid age!")
#
# s1=student("rahul",20)
# print(s1.name)
# print(s1.get_age())
# s1.set_age(22)
# print(s1.get_age())
#
# even_squares=[x**2 for x in range(1,11) if x%2==0]
# print(even_squares)

# even_squares=[x**2 for x in range(1,11) if x%2==0]
# print(even_squares)

# even_squares_dict={x:x**2 for x in range(1,11) if x%2==0}
# print(even_squares_dict)

# even_squares={x**2 for x in range(1,11) if x%2==0}
# print(even_squares)



"""30/01/2025"""
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen=simple_generator()
#
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def my_decorator(func):
#     def wrapper():
#         print("before function execution")
#         func()
#         print("after function execution")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("hello,world")
# say_hello()

""" 1. String → List (Using split())"""

# text='how are you'
# word_list=text.split()
# print(word_list)

"""list to string"""

# word_list=['how','are','you']
# text=' '.join(word_list)
# print(text)


"""reverse string"""
"""using slicing"""

# text="hello"
# reversed_text=text[::-1]
# print(reversed_text)

"""using reversed() and join() """

# text='hello'
# reversed_text="".join(reversed(text))
# print(reversed_text)

"""using loop"""

text="hello"
reversed_text=''

for i in text:
    reversed_text=i+reversed_text
print(reversed_text)