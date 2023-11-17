#Allison Quinn
#11/17/23
#using for loops and the range function
num1 = int(input('Enter a number'))
num2 = int(input('Enter a number'))

if num1 < num2:
    for item in range(num1,num2+1,5):
        print(item)
else:
    print('Second integer cant be less than the first.')
