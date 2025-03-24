

"""Real-time Example:
String: Store product names.
Integer: Store quantities.
Float: Store product prices.
Boolean: Indicate product availability.
List: Store a list of products.
Dictionary: Store product information."""

"""inventory example"""

# product_name = "laptop"
# product_price = 1500.50
# product_quantity = 20
# product_availability = True

"""using list to store multiple products"""
# products=["laptop","smartphone","tablet"]
#
# product_details={"name":product_name,"price":product_price,"quantity":product_quantity,"availability":product_availability}
#
# print(product_details)
#
# print("product_name:",product_details["name"])
# print("product_price:",product_details["price"])
# print("product_quantity:",product_details["quantity"])
# print("product_availability:",product_details["availability"])
#
# print("\nlist of products:",products)


"""conditional statements (if,elif,else)"""
# def apply_discount(price):
#     if price >1000:
#         discount=price*0.10
#         final_price=price-discount
#         print(f"discount applied !final price:${final_price}")
#
#     elif price <= 1000 and price >500 :
#         print(f"no discount.price${price}")
#
#     else:
#         print(f"no discount.item is cheap!")
#
# apply_discount(10000)
# apply_discount(1000)
# apply_discount(100)


"""loops (for and while loop)"""

# products_stock={"laptop":3,"smartphone":8,"tablet":2}
#
# for product,stock in products_stock.items():
#     if stock < 5:
#         print(f"warning {product} needs to restocked (only {stock} left)")
#
#     else:
#         print(f"{product} is in good stock (stock {stock})")


"""while loop"""

# def get_valid_quantity():
#     while True:
#         quantity=input("enter quantity(must be a positive integer):")
#         if quantity.isdigit() and int(quantity) >0:
#             print(f"valid quantity entered:{quantity}")
#         else:
#             print("invalid input!please enter a positive integer")
#
# get_valid_quantity()


"""functions"""

# def calculate_total_cost():
#     total_cost=sum(prices)
#     return total_cost
#
# prices=[1500.50,800.75,300.40]
#
# total=calculate_total_cost()
#
# print(f"total cost of products:${total}")


# orders=[
#         {"product":"laptop","quantity":1},
#         {"product":"smartphone","quantity":2},
#         {"product":"tablet","quantity":3}
# ]
#
# for order in orders:
#     print(f"product: {order['product']},quantity:{order["quantity"]}")





# try:
#     file = open("myfile.txt", "x")  # Create a new file
#     print("File created successfully!")
#     file.close()
# except FileExistsError:
#     print("File already exists!")

# file = open("myfile.txt", "w")  # Create file or overwrite if it exists
# file.write("This is my new file.")
# file.write("\nthis file  recently created")
# file.write("\nthis file  recently created")# Write content
# file.close()
# print("File written successfully!")


"""customer information"""

# customers={"mahendra": {"contact":"123456","address":"hyderabad"},
#            "manikanta": {"contact":"987456","address":"kakinada"}}
#
#
# customer_name="mahendra","maikanta"
# print(f"customer:{customer_name}")
# print(f"contact:{customers[customer_name]['contact']}")
# print(f"address:{customers[customer_name]['address']}")


# import time
#
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Capture start time
#         result = func(*args, **kwargs)  # Call the function
#         end_time = time.time()  # Capture end time
#         print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
#         return result
#     return wrapper
#
# @timer_decorator
# def process_inventory():
#     time.sleep(2)  # Simulate processing
#     print("Inventory processed.")
#
# process_inventory()


"""storing user information"""

# name="mahendra"
# age=30
# print(f"user:{name},age:{age}")

"""product details"""

# product={"name":"laptop","price":1000.50,"quantity":5}
#
# print(f"product:{product['name']},price:{product['price']},quantity:{product['quantity']}")


# a=1,2,3
# print(a)

# schedule=[("09:00","meeting with team"),("11:00","client call"),("14:00","lunch break")]
#
# for time,task in schedule:
#     print(f' at {time}, task:{task}')
#

# fruits=[("100","20 apples"),("200","50 banana"),("300","10 pomegranate")]
#
# for cost,fruit in fruits:
#     print(f" at cost {cost}, quantity:{fruit}")


# import math as m
#
# result = m.pow(5.2915, 2)
# print(result)  # Output: 8.0

# numbers = [1, 2, 3, 4, 5]
#
# # Using lambda with map to double the numbers
# doubled_numbers =list( map(lambda x: x * 2, numbers))

# # Converting map object to list and printing it
# print((doubled_numbers))



"""13-02-2025"""

# import threading
# import time
#
# def print_numbers():
#     for i in range(5):
#         print(i)
#         time.sleep(1)
#
# def print_letters():
#     for letter in 'ABCDE':
#         print(letter)
#         time.sleep(1)
#
# # Creating threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# # Starting threads
# thread1.start()
# thread2.start()
#
# # Waiting for threads to finish
# thread1.join()
# thread2.join()


"data asking data, storing and reading"

# def store_user_data():
#     name=input("enter your name: ")
#     age=input("enter your age: ")
#     email=input("enter your mail: ")
#
#     # with open("user_data.txt","x") as file:
#     #     file.close()
#     # print("file created")
#
#     with open("user_data.txt","a") as file:
#         file.write(f"\n")
#         file.write(f"\nname:{name}\nage:{age}\nemail:{email}")
#
#     print("data saved successfully")
#
# def read_user_data():
#     try:
#         with open("user_data.txt","r") as file:
#             print("\nstored user data:")
#             print(file.read())
#
#     except FileNotFoundError:
#         print("no data found")
# store_user_data()
# read_user_data()

"""simple calculator"""

# def add(x,y):
#     return x+y
#
# def subtract(x,y):
#     return x-y
#
# def multiply(x,y):
#     return x*y
#
# def divide(x,y):
#     try:
#         return x/y
#     except ZeroDivisionError:
#         return "Error: Division by zero"
#
# def calculator():
#     while True:
#         print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
#         choice =input("choose an operation: ")
#
#         if choice == "5":
#             print("Goodbye!")
#             break
#
#         num1= input("Enter first number: ")
#         num2= input("Enter second number: ")
#
#         try:
#             num1=float(num1)
#             num2=float(num2)
#
#         except ValueError:
#             print("Invalid input. Please enter numeric values")
#             continue
#
#         if choice=="1":
#             print("Result:",add(num1,num2))
#         elif choice=="2":
#             print("Result:",subtract(num1,num2))
#         elif choice =="3":
#             print("Result:",multiply(num1,num2))
#         elif choice== "4":
#             print("Result:",divide(num1,num2))
#         else:
#             print("Invalid choice.Try again.")
#
# calculator()

"""simple calculator"""

# def calculator():
#     num1=float(input("Enter first number: "))
#     operator=input("Input operator(+,-,*,/):")
#     num2=float(input("Enter second number: "))
#
#     if operator == "+":
#         print("Result:",num1+num2)
#     elif operator == "-":
#         print("Result :",num1-num2)
#     elif operator == "*":
#         print("Result:",num1*num2)
#     elif operator == "/":
#         print("result:",num1/num2 if num2 !=0 else "Error : Division by zero")
#     else:
#         print("Invalid Operator")
#
# calculator()

# def login_system():
#     # Predefined credentials
#     credentials = {"mahendra@123": "mahendra"}
#
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#
#     if credentials.get(username) == password:
#         print("Login successful! Welcome.")
#     else:
#         print("Invalid username or password.")
#
# login_system()

# Dictionary to map user input to functions
# operations = {
#     '1': lambda x, y: x + y,
#     '2': lambda x, y: x - y,
#     '3': lambda x, y: x * y,
#     '4': lambda x, y: x / y if y != 0 else "Error: Division by zero"
# }
#
# print("Simple Calculator")
# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
#
# choice = input("Enter choice (1/2/3/4): ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# # Get the function from the dictionary and call it
# result = operations.get(choice, lambda x, y: "Invalid choice")(num1, num2)
# print("Result:", result)


# class HospitalBilling:
#     def __init__(self, patient_name, room_type, days_stayed):
#         self.patient_name = patient_name
#         self.room_type = room_type
#         self.days_stayed = days_stayed
#         self.room_rates = {'General': 100, 'Private': 200, 'VIP': 500}
#         self.services = {'Consultation': 50, 'Surgery': 500, 'X-Ray': 100, 'Blood Test': 30}
#         self.total_cost = 0
#
#     def calculate_room_charge(self):
#         return self.room_rates.get(self.room_type, 0) * self.days_stayed
#
#     def calculate_service_charge(self, selected_services):
#         service_cost = sum(self.services.get(service, 0) for service in selected_services)
#         return service_cost
#
#     def calculate_total_cost(self, selected_services):
#         room_charge = self.calculate_room_charge()
#         service_charge = self.calculate_service_charge(selected_services)
#         self.total_cost = room_charge + service_charge
#         return self.total_cost
#
# # Collecting patient information
# patient_name = input("Enter patient's name: ")
# room_type = input("Enter room type (General/Private/VIP): ")
# days_stayed = int(input("Enter number of days stayed: "))
# selected_services = input("Enter selected services (Consultation, Surgery, X-Ray, Blood Test) separated by commas: ").split(',')
#
# # Creating an instance of HospitalBilling
# billing = HospitalBilling(patient_name, room_type, days_stayed)
#
# # Calculating total bill
# total_bill = billing.calculate_total_cost([service.strip() for service in selected_services])
#
# print(f"\n--- Billing Summary for {patient_name} ---")
# print(f"Room charge for {room_type} room for {days_stayed} days: ${billing.calculate_room_charge()}")
# print(f"Service charges: ${billing.calculate_service_charge([service.strip() for service in selected_services])}")
# print(f"Total bill: ${total_bill}")



