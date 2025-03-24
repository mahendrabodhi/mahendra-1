


"""dictionary methods"""


# employee={"name":"mahendra","age":30,"department":"HR"}
#
# print(employee.get("name"))
# print(employee.get("salary","Not Available"))


"""keys"""

# employee={"name":"ravi","age":30,"dept":"HR"}
# print(employee.keys())


# employee={"name":"mahendra","age":30,"dept":"hr"}
# print(employee.values())

# employee={"name":"mahendra","age":30,"dept":"hr"}
# print(employee.items())


# employee={"name":"mahendra","age":30,"dept":'HR'}
# employee.update({"salary":45000,"company":"TCS"})
# print(employee)

# employee={"name":"mahendra","age":30,"dept":"Hr"}
# dept=employee.pop("dept")
# print(dept)
# print(employee)

# employee={"name":"mahendra","age":30,"dept":"HR"}
# item=employee.popitem()
# print(item)
# print(employee)

# employee={"name":"ravi","age":30,"dept":"HR"}
# employee.clear()
# print(employee)

# emp={1}
# emp.clear()
# print(emp)


# Creating an empty set
# empty_set = set()
# # Displaying the empty set
# print(empty_set)
# # Checking its type
# # print(type(empty_set))
#
# empty_set.add(10)
# print(empty_set)  # Output: {10}

# employee={"name":"ravi","age":30}
# employee_copy=employee.copy()
# print(employee_copy)
# print(employee)

# keys=["name","age","dept"]
# default_value=None
# employee=dict.fromkeys(keys,default_value)
# print(employee)


"""for loop"""
# for i in range(5):
#     print(i)

# fruits=["apple","banana","guava","mango"]
# for fruit in fruits:
#     print("I Like ",fruit)


# numbers=[10,15,20,25,30,35]
# for number in numbers:
#     if number%2==0:
#         print("even number:",number)


# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i}x{j}={i*j}")

# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i}x{j}={i*j}")
#     print("------")

# for i in range(1,3):
#     for j in range(1,3):
#         for k in range(1,3):
#             print(i*j*k)

"""26-02-2025"""

# i=1
# while i <=5:
#     print(i)
#     i+=1

"""print even numbers"""
# i=2
# while i<=10:
#     print(i)
#     i+=2

"""print manipulation table"""

# num=3
# i=1
# while i<=10:
#     print(f"{num}x{i}={num*i}")
#     i+=1

"""sum of first 10 natural numbers"""

# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
#     print("sum",sum)

#
# num = 12345
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print("Reversed Number:", rev)



# num=6
# factorial=1
# i=1
#
# while i<=num:
#     factorial*=i
#     i+=1
#     print(f"factorial of {num} is {factorial}")


"""fibonaci sequence"""

# a,b=0,1
# i=1
# while i<=10:
#     print(a,end=" ")
#     a,b=b,a+b
#     i+=1



"""functions"""
# def find_max(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(find_max(10,20))

"""*args"""

# def add(*args):
#     return max(args)
# var=add(10,20,30,40)
# print(var)

# def check_evn_odd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
#
# print(check_evn_odd(7))
# print(check_evn_odd(8))


# class Animal:
#     def __init__(self,type,colour,place):
#         self.type=type
#         self.colour=colour
#         self.place=place
#     def show_details(self):
#         print(f"Animal type:{self.type},colour:{self.colour},place:{self.place}")
#
# animal1=Animal("cow","white","rajahmundry")
#
# animal1.show_details()

"""reverse string"""


# def reverse_string(s):
#     return s[::-1]
#
# print(reverse_string("hello"))



# string="hello"
# reverse_string=""
#
# for i in string:
#     reverse_string=i+reverse_string
# print(reverse_string)


"""check a number is prime"""

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,int(n**.5)+1):
#         if n %i==0:
#             return False
#     return True
#
# print(is_prime(7))
# print(is_prime(8))

"""print prime"""


# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**.5)+1):
#         if n%2==0:
#             return False
#     return True
#
# def print_primes_below_100():
#     for num in range(2,100):
#         if is_prime(num):
#             print(num,end=" ")
#
# print_primes_below_100()

"""*args"""
# def sum_all(*args):
#     return sum(args)
#
# print(sum_all(1,2,3,4,5))
# print(sum_all(1000,1000))



# def find_max(*args):
#     return max(args)
#
# print(find_max(10,100,1000))
# print(find_max(2.5,3.5,7.9))


"""concatenate strings"""

# def join_strings(*args):
#     return " ".join(args)
#
# print(join_strings("hello","world"))
# print(join_strings("python","is","awesome"))


# def multiply_all(*args):
#     result=1
#     for num in args:
#         result*=num
#     return result
# print(multiply_all(2,3,4,5))


# def add_all(*args):
#     result=0
#     for num in args:
#         result+=num
#     return result
#
# print(add_all(10,100,1000))


"""function to print all arguments"""

# def print_args(*args):
#     for arg in args:
#         print(arg)
#
# print_args(1,2,3,"python",[10,20,30])


"""function to print key-value pairs"""


# def print_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
#
# print_details(name="manikanta",age="25",city="rajahmundry")


# def student_profile(**kwargs):
#     return kwargs
#
# profile=student_profile(name="mahendra",marks=92,school="gowtham")
# print(profile)



"""function with default and additional arguments"""

# def display_info(name,age,**kwargs):
#     print(f"name:{name},age:{age}")
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
#
# display_info("mahesh",25,city="amaravathi",job="Developer")


# def configure_settings(defaults,**custom):
#     settings=defaults.copy()
#     settings.update(custom)
#     return settings
#
# default_settings={"theme":"light","font_size":12,"language":"english"}
# user_settings=configure_settings(default_settings,theme="dark",font_size=14)
#
# print(user_settings)

"""lambda arguments"""

# add=lambda a,b:a+b
# print(add(5,6))

# maximum=lambda a,b:a if a>b else b
# print(maximum(10,202))
# print(even_odd(5))

# square=lambda x:x**2
# print(square(5))

"find the cube of a number"

# cube=lambda x:x**3
# print(cube(3))


# string_length=lambda s:len(s)
# print(string_length("hello"))

# numbers=[1,2,3,4,5,6,7,8,9]
# even_numbers=list(filter(lambda x:x%2==0,numbers))
# print(even_numbers)

# numbers=[1,2,3,4,5,6,7,8,9]
# double_numbers=list(map(lambda x:x*2,numbers))
# print(double_numbers)


"""lambda with reduce"""
# from functools import reduce
#
# numbers=[1,2,3,4,5,6]
# sum_numbers=reduce(lambda x,y:x+y,numbers)
# print(sum_numbers)

"""sort a list of tuples by second element"""

# students=[("rakesh",85),("mahesh",89),("suresh",77)]
# sorted_students=sorted(students,key=lambda x:x[1])
# print(sorted_students)


"""generator"""

# def simple_generator():
#     for num in range(1,7):
#         yield num
#
# gen=simple_generator()
# for num in gen:
#     print(num)

# def even_numbers(n):
#     for i in range(2,n+1,2):
#         yield i
#
# gen=even_numbers(10)
# print(list(gen))

# def fibonacci(n):
#     a,b=0,1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
#
# gen=fibonacci(10)
# print(list(gen))

# def countdown(n):
#     while n>0:
#         yield n
#         n-=1
#
# gen=countdown(5)
# print(list(gen))

# def squares(n):
#     for i in range(1,n+1):
#         yield i**2
#
# gen=squares(5)
# print(list(gen))


# def my_decorator(func):
#     def wrapper():
#         print("function is being executed")
#         func()
#     return wrapper
# @my_decorator
#
# def say_hello():
#     print("hello,world")
# say_hello()

# def log_function(func):
#     def wrapper(*args,**kwargs):
#         print(f"calling {func.__name__} with arguments {args}{kwargs} ")
#         return func(*args,**kwargs)
#     return wrapper
#
# @log_function
# def add(a,b):
#     return a+b
# print(add(1,2))


"""overloading"""

# class MathOperations:
#     def add(self,a,b=0,c=0):
#         return a+b+c
#
# math_obj=MathOperations()
# print(math_obj.add(10))
# print(math_obj.add(10,20))
# print(math_obj.add(10,20,30))

# class Mathoperations:
#     def add(self,*args):
#         return sum(args)
#
# math_obj=Mathoperations()
#
# print(math_obj.add(10,20))
# print(math_obj.add(30,40,50))


"""method overriding"""



"""Basic Method Overriding Example"""
# class parent:
#     def show(self):
#         print("this is parent class")
#
# class child(parent):
#     def show(self):
#         print("this is child class")
#
# obj=child()
# obj.show()


"""1... Using super() (Recommended)"""
# class lorry:
#     def details(self):
#         print("lorry details")
#
# class bus(lorry):
#     def details(self):
#         super().details()
#         print("car details")
#
#
# obj=bus()
# obj.details()


"""2... Calling Parent.show(self) Directly"""
# class Car:
#     def show(self):
#         print("this is new car")
#
#
# class Car2(Car):
#     def show(self):
#         Car.show(self)
#         print("this is latest version")
#
# obj=Car2()
# obj.show()


"""overriding __init__ constructor"""

# class parent:
#     def __init__(self):
#         print("parent constructor")
#
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("child constructor")
#
# obj=child()


"""27-02-2025"""
# Can you guess the output of this code?
# def mystery_function(x):
#     return (lambda y: y * x)(x + 2)
#
# print(mystery_function(3))
# print(mystery_function(5))


# def tricky_lambda(n):
#     return lambda x:x**n
#
# power_of_2=tricky_lambda(2)
# power_of_3=tricky_lambda(3)
#
# print(power_of_2(4))
# print(power_of_2(2))


# numbers=[1,2,3,4,5]

# result=list(map(lambda x:x*2 if x%2==0 else x+1 ,numbers))
#
# print(result)


# numbers=[1,2,3,4,5]
#
# result=list(map(lambda x:x/2 if x%2==0 else x*3,numbers))
#
# print(result)


# numbers=[1,2,3,4,5]
#
# result=list(map(lambda x:x**2 if x%2==0 else x**3,numbers))
#
# print(result)


# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# numbers=[1,2,3,4,5,6,7,8,9,10]
#
# result=list(map(lambda x:x if is_prime(x) else x*2,numbers))
#
# print(result)
#
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**.5)+1):
#         if n%i==0:
#             return False
#     return True
# #
# numbers=[1,2,3,4,5,6,7,8,9,10]

# result=list(map(lambda x:x  if is_prime(x) else (x*3 if x%2==0 else x/2),numbers))
#
# print(result)

# result=list(map(lambda x:x**2 if is_prime(x) else (x/2 if x%2==0 else x),numbers))
#
# print(result)

# result=list(map(lambda x:x if is_prime(x) else (x*4 if x%2==0 else x-1),numbers))
#
# print(result)


# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**.5)+1):
#         if n%i==0:
#             return False
#     return True
# #
# numbers=[1,2,3,4,5,6,7,8,9,10]
#
# result=list(map(lambda x:x*2 if is_prime(x) else (x/2 if x%2==0 else x**3 ),numbers))
#
# print(result)

# numbers=[1,2,3,4,5]
# new_list=[]
#
# for i in numbers:
#     if i%2==0:
#         new_list.append(i**2)
#     else:
#         new_list.append(i*3)
# print(new_list)


# names = ["Alice", "Bob", "Charlie"]
#
# dict_names={}
#
# for name in names:
#     dict_names[name]=len(name)
# print(dict_names)


# names=["mahendra","ramu","sai"]
#
# dict_names={}
# for name in names:
#     dict_names[name]=len(name)
# # print(dict_names)
#
# sorted_dict=dict(sorted(dict_names.items(),key=lambda item:item[1]))
# print(sorted_dict)


# people=[("Alice",25),("Bob",17),("Charlie",19),("David",15)]
# new_list=[]
#
# for name,age in people:
#     if age >18:
#         new_list.append(name)
# print(new_list)

# numbers=[1,2,2,3,4,4,5,6,6,7]
# new_list=set(numbers)
# print(list(new_list))

# new_list=[]
# for number in numbers:
#     if number not in new_list:
#         new_list.append(number)
# print(new_list)
#
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result*=i
#     return result
# print(factorial(5))


# s="hello world"
# char_count={}
#
# for char in s:
#     if char in char_count:
#         char_count[char]+=1
#     else:
#         char_count[char]=1
# print(char_count)


# numbers=[10,15,20,25,30,35,40]

# for number in numbers:
#     if number%2!=0:
        # print(number)

# odd_numbers=[]
#
# for number in numbers:
#     if number%2!=0:
#         odd_numbers.append(number)
# print(odd_numbers)


# numbers=[10,25,5,40,15]
# max_number=numbers[0]
#
# for number in numbers:
#     if number>max_number:
#         max_number=number
#
# print(max_number)

# numbers=[2,3,2,5,3,7,5,2,8,3]
# dict_number={}
#
# for number in numbers:
#     if number in dict_number:
#         dict_number[number]+=1
#     else:
#         dict_number[number]=1
# print(dict_number)
#
# text="hello"
# reversed_text=""
# for i in text:
#     reversed_text=i+reversed_text
# print(reversed_text)


# numbers=[10,25,5,40,15]
# first_largest=0
# second_largest=0
#
# for number in numbers:
#     if number>first_largest:
#         second_largest=first_largest
#         first_largest=number
#     elif number>second_largest and number!=first_largest:
#         second_largest=number
# print(second_largest)


# text="hello world"
# counter=0
# for letter in text:
#     if letter in "aeiouAEIOU":
#         counter+=1
#
# print(counter)
#
# numbers=[10,25,5,40,15]
# largest_number=0
#
# for number in numbers:
#     if number>largest_number:
#         largest_number=number
# print(largest_number)


# numbers=[1,2,3,4,5]
# reversed_numbers=[]
#
# for number in numbers:
#     reversed_numbers.insert(0,number)
# print(reversed_numbers)


# numbers=[10,25,5,40,15]
#
# smallest=float('inf')
# second_smallest=float('inf')
#
# for number in numbers:
#     if number<smallest:
#         second_smallest=smallest
#         smallest=number
#     elif number<second_smallest and number!=smallest:
#         second_smallest=number
# print(second_smallest)

# numbers=[1,2,3,3,4,4,3,5,6,6,3,7,2,2]
# dict_={}
#
# for i in numbers:
#     if i in dict_:
#         dict_[i]+=1
#     else:
#         dict_[i]=1
# most_frequent=max(dict_,key=dict_.get)
#
# print(most_frequent)




# my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
#
# # Replace key 'city' with 'location'
# my_dict['location'] = my_dict.pop('city')    # Add new key with the value
#
# print(my_dict)
#

# d = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# swapped = {v: k for k, v in d.items()}
# print(swapped)
#


# queue = []
# queue.append(10)  # Enqueue
# queue.append(20)
# print(queue.pop(0))  # Dequeue
# print(queue)



"""* args"""
# def add(*args):
#     return sum(args)
# print(add(5,65))


# def multiply(*args):
#     result=1
#     for num in args:
#         result*=num
#     return result
# print(multiply(2,4,6))


# def multiply(*args):
#     result=1
#     for i in args:
#         result*=i
#     return result
# print(multiply(5,5,5))


# def total(a,b,c):
#     return a+b+c
#
# nums=[1,2,3]
# print(total(*nums))


# def person_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# person_info(name="mahendra",age=25,city="new york")



# def mixed_function(*args,**kwargs):
#     print("positional arguments:",args)
#     print("keyword arguments:",kwargs)
#
# mixed_function(1,2,3,4,name="mahendra",age=25,place="new york")



# def greet(*names, msg="Hello"):
#     for name in names:
#         print(f"{msg}, {name}!")
#
# greet("Alice", "Bob", msg="Hi")


# def greet(*names,msg,quote):
#     for name in names:
#         print(f"{msg},{name},{quote}")
# greet("mahendra","annaya","sanju","dhanu",msg="hai",quote="bye")



# class Car:
#
#     def __init__(self,model,colour,price):
#         self.model=model
#         self.colour=colour
#         self.price=price
#
#     def display_details(self):
#         print(f"model:{self.model}, colour:{self.colour}, price:{self.price}")
#
#
# car1=Car("toyota","black" ,3500000)
# car2=Car("hyundai","white",2000000)
# car3=Car("mahindra","red",2200000)
# car4=Car("tata","blue",1000000)
#
# car1.display_details()
# car2.display_details()
# car3.display_details()
# car4.display_details()


# class Parent:
#     def show(self):
#         print("this is parent class")
#
# class Child(Parent):
#     def show(self):
        # super().show()
        # Parent.show(self)
#         print("this is child class")
#
# child=Child()
# child.show()

# class example:
#     def show(self,*args):
#         print("Arguments passed:",args)
#
# obj=example()
# obj.show()
# obj.show(5)
# obj.show(5,10,15)
#
# class Grandparent:
#     def display(self):
#         print("this is grandparent class")
#
# class Parent(Grandparent):
#     def display(self):
#         super().display()
#         print("this is parent class")
#
# class Child(Parent):
#     def display(self):
#         super().display()
#         print("this is child class")
#
# c=Child()
# c.display()


# class Calculator:
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
#
# calc=Calculator()
# print(calc.add())
# print(calc.add(5))
# print(calc.add(5,10))
# print(calc.add(5,10,15))



# def log_decorator(func):
#     def wrapper():
#         print(f"before  {func.__name__}")
#         func()
#         print(f"after  {func.__name__}")
#     return wrapper
#
# @log_decorator
# def say():
#     print("hello ")
# @log_decorator
# def greet():
#     print("bye")

# say()
# greet()
#
# def log_decorator(func):
#     def wrapper():
#         print(f"Calling function: {func.__name__}")
#         func()
#         print(f"Function {func.__name__} executed successfully.")
#     return wrapper
#
# @log_decorator
# def greet():
#     print("Hello, World!")
# @log_decorator
# def say_bye():
#     print("Goodbye!")
#
# greet()
# say_bye()



# text="hello"
# upperr=text.upper()
# print(upperr)
#

"""operator overloading"""

# class Student:
#     def __init__(self, marks):
#         self.marks = marks
#
#     def __add__(self, other):  # Overloading `+` operator
#         return self.marks + other.marks
#
#
# s1 = Student(85)
# s2 = Student(90)
#
# print(s1 + s2)  # Calls __add__()


"""encapsulation ---public encapsulation """
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name  # Public variable
#         self.salary = salary  # Public variable
#
#     def show(self):
#
#         print(f"Employee Name: {self.name}, Salary: {self.salary}")
#
#
# emp = Employee("Mahesh", 50000)
# print(emp.name)  # Accessing public variable
# print(emp.salary)  # Accessing public variable
# emp.show()  # Calling public method


"""protected encapsulation"""

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self._balance=balance
#
#     def show_balance(self):
#         print(f"Account Owner:{self.owner},balance :{self._balance}")
#
# class SavingsAccount(BankAccount):
#     def access_balance(self):
#         print(f"Accessing balance inside subclass:{self._balance}")
#
# acc=SavingsAccount("Manikanta",10000)
# print(acc.owner)
# print(acc._balance)
# acc.access_balance()




# class Student:
#     pass  # No __init__
#
# # Creating instance
# s1 = Student()
#
# # Setting attributes manually (not recommended)
# s1.name = "Rakesh"
# s1.age = 20
#
# print(s1.name, s1.age)  # Output: Rakesh 20


