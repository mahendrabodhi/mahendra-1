


"""one"""

# import threading
# import time
#
# def print_numbers():
#     for i in range(1,6):
#         print(f"number: {i}")
#         time.sleep(1)
#
# def print_letters():
#     for letter in ['a','b','c','d','e']:
#         print(f"letter: {letter}")
#         time.sleep(1)
#
# thread1=threading.Thread(target=print_numbers)
# thread2=threading.Thread(target=print_letters)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("both threads finished")


# import multiprocessing
#
# import time
#
# def print_numbers():
#     for i in range(1,6):
#         print(f"number: {i}")
#         time.sleep(1)
#
# def print_letters():
#     for letter in ['A','B','C','D','E']:
#         print(f"letter :{letter}")
#         time.sleep(1)
#
# if __name__=="__main__":
#
#     process1=multiprocessing.Process(target=print_numbers)
#     process2=multiprocessing.Process(target=print_letters)
#
#     process1.start()
#     process2.start()
#
#     process1.join()
#     process2.join()
#
#     print("Both processes finished")


# import threading
#
# def say_hello():
#     print("hello from thread")
#
# t1=threading.Thread(target=say_hello)
#
# t1.start()
#
# t1.join()
#
# print("main program ends")


# import threading
# import time
# #
# def print_numbers():
#     for i in range(1,6):
#         print(f"number:{i}")
#         time.sleep(1)
#
# def print_letters():
#     for letter in['A','B','C','D','E']:
#         print(f"letter:{letter}")
#         time.sleep(1)
#
# def print_words():
#     for word in['hai','how','are','you','doing']:
#         print(f"word:{word}")
#         time.sleep(1)
# #
# t1=threading.Thread(target=print_numbers)
# t2=threading.Thread(target=print_letters)
# t3=threading.Thread(target=print_words)
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
#
# print("both threads finished")


# import threading
#
# counter = 0
# lock = threading.Lock()
#
# def increment():
#     global counter
#     for _ in range(100000):
#         with lock:
#             counter += 1
#
# threads = []
# for _ in range(5):
#     t = threading.Thread(target=increment)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print("Counter Value:", counter)


# class Parent:
#     def show(self):
#         print("👨‍👦 Parent class")
#
# class Child(Parent):
#     pass
#
# c = Child()
# c.show()  # Output: 👨‍👦 Parent class
#
# # Check MRO
# print(Child.mro())


# class Parent:
#     def show(self):
#         print("Parent class")
#
# class Child(Parent):
#     pass
#
# c=Child()
# c.show()
#
# print(Child.mro())



# class A:
#     def show(self):
#         print("Class A")
#
# class B(A):
#     def show(self):
#         print("Class B")
#
# class C(A):
#     def show(self):
#         print("Class C")
#
# class D(B,C):
#     pass
#
# d=D()
# d.show()
#
# print(D.mro())

# class LoggerMixin:
#     def process_request(self):
#         print("logging the request")
#
# class AuthenticationMixin:
#     def process_request(self):
#         print("Authenticating the request")
#
# class APIHandler(LoggerMixin,AuthenticationMixin):
#     def process_request(self):
#         print("Handling the API request")
#         super().process_request()
# handler=APIHandler()
#
# handler.process_request()
#
# print("\n method resolution order:",[cls.__name__ for cls in APIHandler.__mro__])


# import multiprocessing
# import time
#
# def print_numbers():
#     for i in range(7):
#         print(f"Number: {i}")
#         time.sleep(1)
#
# if __name__ == '__main__':
#     # Creating four processes
#     p1 = multiprocessing.Process(target=print_numbers)
#     p2 = multiprocessing.Process(target=print_numbers)
#     p3 = multiprocessing.Process(target=print_numbers)
#     p4 = multiprocessing.Process(target=print_numbers)
#     # Starting the processes
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     # Wait for both processes to finish
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     print("Both processes completed.")




