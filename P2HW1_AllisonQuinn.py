#Allison Quinn
#10/5/2023
#Introduction to dictionaries

#Get input from user
name = input('Enter your name: ')
hair = input('Enter your hair color: ')
eye = input('Enter your eye color ')
height = float(input('Enter height as a decimal: '))
age = int(input('Enter your age: '))
food = input('Whats your favorite food? ')

#Create a dictionary - curly barces
my_dict = {'Name': name, 'Hair_Color': hair, 'Eye_Color': eye, 'Height': height, 'Age': age, 'Food': food}

#Get values using the key
print(f"{my_dict['Name']} is a {my_dict['Height']} tall student with {my_dict['Hair_Color']} hair and {my_dict['Eye_Color']} eyes. they are {my_dict['Age']} years old and their favorie food is {my_dict['Food']}")
