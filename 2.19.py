# list=[]
# print(not list)

# a=10
# # a//=3
# # print(a)
#
# a/=3
# print(a)

# Install library: pip install kafka-python
# from kafka import KafkaProducer, KafkaConsumer
#
# # Producer (sends messages to Kafka topic)
# producer = KafkaProducer(bootstrap_servers='localhost:9092')
# producer.send('my_topic', b'Hello Kafka from Python!')
# producer.close()
#
# # Consumer (reads messages from Kafka topic)
# consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092')
# for message in consumer:
#     print(f"Received message: {message.value.decode('utf-8')}")
#
#

# def get_first_element(lst):
#     return lst[0]  # Accessing takes constant time

# age = 20
# if age < 18:
#     print("Eligible to vote")  # Logical mistake
# else:
#     print("Not eligible to vote")

# a=set()
# print(type(a))

# def my_func(a,b):
#     return a+b
# result=my_func('hello','hello')
# print(result)


# a=[1,2,3,4]
# b=[1,2,3]
#
# print(a+b)