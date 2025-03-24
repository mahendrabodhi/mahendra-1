

# dict={'name':'mahendra','place':'burugupudi'}
# dict['location']=dict.pop('place')
# print(dict)



strings = ['one', 'two', 'three', 'four', 'five', 'eleven', 'twenty-two']

# Initialize a variable to store the largest string by length
largest_string = ''

for string in strings:
    if len(string) > len(largest_string):  # Compare the length of each string
        largest_string = string  # Update the largest string

print("Largest string by length:", largest_string)


strings = ['one', 'two', 'three', 'four', 'five', 'eleven', 'twenty-two']

# Initialize variables for largest and second largest strings by length
largest_string = ''
second_largest_string = ''

for string in strings:
    if len(string) > len(largest_string):  # If current string is longer than the largest_string
        second_largest_string = largest_string  # Update second largest
        largest_string = string  # Update largest
    elif len(string) > len(second_largest_string) and string != largest_string:
        second_largest_string = string  # Update second largest if it's not the largest

print("Largest string by length:", largest_string)
print("Second largest string by length:", second_largest_string)
