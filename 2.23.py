"""list methods"""


# fruits=["sapota","watermelon"]
# fruits.append("muskmelon")
#
# print(fruits)

# data=[12,25,19,9,7,6,101]
# data.sort()
# print(data)

# from_data=['username','mail']
# additional_data=['password','confirm_password']
# from_data.extend(additional_data)
# print(from_data)

# labels=['spam','ham','spam','spam','ham']
# spam_count=labels.count('spam')
# ham_count=labels.count('ham')
# print(f"spam:{spam_count},ham:{ham_count}")

# inventory=["laptop","mouse","keyword"]
# new_product="monitor"
# inventory.append(new_product)
# print(inventory)

# tasks=["buy groceries","pay bills"]
# new_tasks=["call plumber","book tickets"]
# tasks.extend(new_tasks)
# print(tasks)

# name="manikanta"
# print(name)

# tasks=["task1","task3"]
# tasks.insert(1,"task2")
# print(tasks)

# cart=["shoes","shirt","watch"]
# cart.remove("shirt")
# print(cart)


# actions=["type A","type B","delete B"]
# last_action=actions.pop()
# print("union:",last_action)
# print(actions)


# options=["A","B","C","D"]
# correct=options.index("B")
# print(correct)

# things=["door","house","bed","book"]
# things.pop()
# print(things)
# thing=things.index("house")
# print(thing)


# votes=["A","b","c","A","A","D"]
# a_votes=votes.count("A")
# print("candidate A got",a_votes, "votes")

# prices=[499,399,299,578,422]
# prices.sort()
# print(prices)

# prices.sort(reverse=True)
# print(prices)

# messages=["Hello","How are you?","Bye"]
# messages.reverse()
# print(messages)

# data=["file1","file2","file3"]
# backup=data.copy()
# print("backup data:",backup)


# cart=["item1","item2","item3"]
# cart.clear()
# print(cart)



"""24-02-2025"""

# a=1,2,3
# print(a)



# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
#
# class Dog(Animal):
#     def sound(self):
#         super().sound()  # Calls superclass method
#         print("Dog barks")
#
# d = Dog()
# d.sound()

# notifications=['email',"SMS","Push"]
# notifications.clear()
# print(notifications)

# users=["rohit","Swamy","Manoj"]
# print(len(users))

# salaries=[45000,50000,60000,75000]
# highest_salary=max(salaries)
# print(highest_salary)

# temperatures=[22,18,25,19,21]
# lower_temp=min(temperatures)
# print(lower_temp)

# product_prices=[1500,2000,3200,2100]
# print("max product_price:",max(product_prices))
# print("min product_price:",min(product_prices))

# if 5 > 3:
#     print("5 is greater than 3")  # Indented block
# print("Outside the if block")



"""string methods"""

# name="manikanta"
# print(name.upper())

# name="MANIKANTA"
# print(name.lower())

# email="User@Example.COM"
# print(email.lower())

# book="the great gatsby"
# print(book.title())


# text=" Hello World "
# print(text.strip())

# sentence="I love java"
# print(sentence.replace("java","Python"))

# data="apple,banana,orange"
# fruits=data.split(",")
# print(fruits)

# words=["Welcome","to","Python"]
# sentence=" ".join(words)
# print(sentence)


# message="Find the word 'the' in this sentence"
# print(message.find("the"))

# url="https://example.com"
# print(url.startswith("https"))

# file="report.pdf"
# print(file.endswith(".pdf"))

# code="12345"
# print(code.isdigit())

# name="Manikanta"
# print(name.isalpha())

# text="Python is popular because Python is easy"
# print(text.count("s"))

# quote="python is awesome"
# print(quote.capitalize())

# word="hai"
# print(word.islower())

# car="TOYOTA"
# print(car.isupper())

# alpha_numeric="125abcS"
# print(alpha_numeric.isalnum())

# swap="mahendra"
# print(swap.swapcase())


# tuplee=(1,2,3,4,4,4)
# tup=tuplee.count(4)
# print(tup)

# tupple=(1,2,3,4,5)
# tupp=tupple.index(3)
# print(tupp)

"""2.25-02-2025"""

# import threading
# import time
#
# def print_numbers():
#     for number in range(1,6):
#         print(f"number:{number}")
#         time.sleep(1)
#
# def print_names():
#     for name in["mahendra","nagesh","raina","pankaj","suresh"]:
#         print(f"name:{name}")
#         time.sleep(1)
#
#
# thread1=threading.Thread(target=print_numbers)
# thread2=threading.Thread(target=print_names)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()


# import multiprocessing
# import time
#
# def print_cars():
#     for car in["toyota","suzuki","mahendra","tata"]:
#         print(f"car     :{car}")
#         time.sleep(1)
#
# def print_location():
#     for location in["rajahmundry","kakinada","hyderabad","guntur","amaravathi"]:
#         print(f"location:{location}")
#         time.sleep(1)
#
# if __name__=="__main__":
#
#     process1=multiprocessing.Process(target=print_cars)
#     process2=multiprocessing.Process(target=print_location)
#
#
#     process1.start()
#     process2.start()
#
#
#     process1.join()
#     process2.join()


"""set methods"""

# attendance={"S001","S002","S003","S004"}
# attendance.add("S005")
# print(attendance)


# products={"laptop","phone","tablet"}
# products.remove("tablet")
# print(products)

# players={"Tom","Jerry","Spike"}
# players.discard("Butch")
# print(players)

# dept1={"Alice","Bob"}
# dept2={"Charlie","Bob"}
# combined=dept1.union(dept2)
# print(combined)

# data_analyst={"Amit","Rohit","Sneha"}
# software_dev={"Rohit","Sneha","Priya"}
# common=data_analyst.intersection(software_dev)
# print(common)

# active_members={"ramesh","eswar","gowtham","vishnu"}
# paid_members={"eswar","gowtham"}
#
# unpaid_members=active_members.difference(paid_members)
# print(unpaid_members)

# main_library={"book1","book2","book3"}
# branch_library={"book2","book4"}
# unique_books=main_library.symmetric_difference(branch_library)
# print(unique_books)

# high_priority={"task1","task2"}
# completed={"task1","task2","task3"}
# print(high_priority.issubset(completed))


# required_courses={"Math","Science"}
# student_courses={"Math","Science","English"}
# print(student_courses.issuperset(required_courses))

# cart={"item1","item2","item3"}
# cart.clear()
# print(cart)

# contacts=["Alice","Bob","Alice","Tom","Bob","Sam"]
# unique_contacts=set(contacts)
# print(unique_contacts)


# tasks={"Task1","Task2","Task3","Task4"}
# removed_task=tasks.pop()
# print(f"Assigned Task:{removed_task}")
# print(f"Remaining Task:{tasks}")

# guests={"mahendra","gowtham","eswar"}
# new_guests={"mahendra","vishnu","krishna"}
# guests.update(new_guests)
# print(guests)


# team1_A={"virat","shreyas","subman"}
# team1_B={"ronaldo","messi","neymar"}
#
# no_common_players=team1_A.isdisjoint(team1_B)
# print(no_common_players)


"""for loop"""

"""iterate over a list"""
# products=["laptop","Mobile","Tablet","headphones"]
#
# for product in products:
#     print("Product available:",product)


"""iterate using range()"""
# for order_id in range(1001,1006):
#     print("Order ID:",order_id)


"""loop through a dictionary"""

# employees={"mahendra":"software","harish":"analytics","revanth":"cloth_merchant"}
#
# for name,dept in employees.items():
#     print(f"employee:{name},department:{dept}")


"""Nested for loop"""
# rows=["A","B","C"]
# seats=[1,2,3,4]
# for row in rows:
#     for seat in seats:
#         print(f"seat:{row}{seat}")


"""using for loop with if condition"""

# inventory={"laptop":5,"Mobie":0,"Tablet":4,"Headphones":0}
#
# for product,stock in inventory.items():
#     if stock ==0:
#         print(f"{product} is out of stock")



# from multiprocessing import Process
# import os
#
# # Function to be executed by each process
# def print_square(number):
#     print(f"Process ID: {os.getpid()} → Square of {number}: {number ** 2}")
#
# if __name__ == "__main__":
#     # List of numbers to process
#     numbers = [1, 2, 3, 4, 5]
#
#     # List to hold process objects
#     processes = []
#
#     # Creating processes
#     for num in numbers:
#         process = Process(target=print_square, args=(num,))
#         processes.append(process)
#         process.start()  # Start the process
#
#     # Joining processes to wait for their completion
#     for process in processes:
#         process.join()
#
#     print(" All processes completed!")


# class Example:
#     # Class Variable
#     class_var = "Shared Across All Instances"
#
#     def __init__(self, name):
#         # Instance Variable
#         self.name = name
#
#     # Instance Method (uses self)
#     def show_name(self):
#         print(f"Instance Name: {self.name}")
#
#     # Class Method (uses cls)
#     @classmethod
#     def show_class_var(cls):
#         print(f"Class Variable: {cls.class_var}")
#
#     # Static Method (no self or cls)
#     @staticmethod
#     def greet():
#         print("Hello! I'm a static method.")
#
# # Creating an instance
# obj = Example("Raj")
#
# # Instance Method
# obj.show_name()            # Output: Instance Name: Raj
#
# # Class Method
# Example.show_class_var()    # Output: Class Variable: Shared Across All Instances
#
# # Static Method
# Example.greet()             # Output: Hello! I'm a static method.


# employee={"name":"ravi","age":"25","dept":"hr"}
#
# print(employee.get("name"))
# print(employee.get("salary","note available"))


"""26-02-2025"""

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