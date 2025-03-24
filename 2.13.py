""""""

# def is_prime(n):



# for i in range(1,10):
#     if i%2==0:
#         print("number is even:",i)
#
#     else:
#         print("number is odd :",i)


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# # Test the function
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")




# def voter_eligibility(func):
#     def wrapper(age):
#         print(f"checking age eligibility")
#         if age>=18:
#             func(age)
#         else:
#             print(f"not eligible for vote")
#     return wrapper
# @voter_eligibility
# def voter(age):
#     print(f"eligible to vote age is :{age}")
#
# voter(19)
# voter(17)

# import psycopg2
#
# try:
#     # Establish connection
#     conn = psycopg2.connect(
#         host="localhost",
#         database="2025-jan",
#         user="postgres",
#         password="mahendra"
#     )
#
#     # Create a cursor
#     cur = conn.cursor()
#
#     # Execute a query
#     cur.execute("SELECT * FROM transport ;")
#     rows = cur.fetchall()
#
#     # Print the results
#     for row in rows:
#         print(row)
#
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     # Close cursor and connection
#     if cur:
#         cur.close()
#     if conn:
#         conn.close()





# nums = [1, 2, 3, 4, 5]
# even_nums = filter(lambda x: x % 2 == 0, nums)
# print((even_nums))  # Output: [2, 4]



# def double(x):
#     return x * 2
# nums=[1,2,3,4,5]
# doubled = [double(x) for x in nums]
# print(doubled)  # Output: [2, 4, 6, 8, 10]

"""delete duplicates"""
# l1 = [10, 20, 20, 30, 40]
# unique_list = []
#
# # Using a loop to keep only unique elements
# for item in l1:
#     if item not in unique_list:
#         unique_list.append(item)
#
# print(unique_list)

""""""
# input_list = [1, [2, 3], 4, [5, 6, 7]]
# flat_list = []
#
# # Loop through each element in the input list
# for item in input_list:
#     if isinstance(item, list):   # Check if the item is a list
#         flat_list.extend(item)   # Add all elements of the nested list to flat_list
#     else:
#         flat_list.append(item)   # Add the non-list item directly
#
# print(flat_list)

"""flatten list"""
# list1=[1,2,3,4,5,[6,7],8,[9,10]]
#
# flat_list=[]
#
# for item in list1:
#     if isinstance(item,list):
#         flat_list.extend(item)
#     else:
#         flat_list.append(item)
# print(flat_list)


# from functools import reduce
#
# list1 = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flat_list = reduce(lambda x, y: x + y, list1)
# print(flat_list)

# list_of_sets = [{1, 2}, {3, 4}, {5, 6}]
# flat_list = [item for s in list_of_sets for item in s]
# print(flat_list)


# list_of_sets=[{1,2},{3,4},{5,6}]
# flat_list=[item for s in list_of_sets for item in s]
# print(flat_list)

"""sorting"""

# prices=[499,299,199,899,699,999]
#
# # prices.sort()
# #
# # print(prices)
#
# search_price=899
# if search_price in prices:
#     print(f"price{search_price} found at index:", prices.index(search_price))
# else:
#     print("price not found")

"""flatten_list"""
# input_list=[1,2,[3,4],5,[6,7],8]
# flatten_list=[]
# for item in input_list:
#     if isinstance(item,list):
#         flatten_list.extend(item)
#     else:
#         flatten_list.append(item)
# print(flatten_list)
#

"""flatten_list"""
# input_list=[1,2,3,[4,5],6,[7,8],9]
# flatten_list=[]
#
# for item in input_list:
#     if isinstance(item,list):
#         flatten_list.extend(item)
#     else:
#         flatten_list.append(item)
# print(flatten_list)


# input_list=[1,2,[3,4],5,[6,7],8]
# flatten_list=[]
#
# for item in input_list:
#     if isinstance(item,list):
#         flatten_list.extend(item)
#     else:
#         flatten_list.append(item)
# print(flatten_list)

# my_list = [1, 2, 3]
# print(isinstance(my_list, tuple))  #
#
# my_number = 10
# print(isinstance(my_number, int))


# mixed_list=[1,'hello',3.5,[2,3]]
#
# for item in mixed_list:
#     if isinstance(item,int):
#         print(f"{item} is an integer")
#     elif isinstance(item,str):
#         print(f"{item} is a string")
#     elif isinstance(item,list):
#         print(f"{item} is a list")
#


