print("Input:")
input_string= input()
special=['a','e','i','o','u']
counter=0
'''
Code Description: This code counts the number of vouls in an input string
'''
for character in input_string:
    if character in special:
        counter +=1

print(counter)