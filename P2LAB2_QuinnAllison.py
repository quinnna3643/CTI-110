#Allison Quinn
#10/5/2023
#Formatting Floats

#Get float input from user
num1 = float(input("Enter a value "))
num2 = float(input("Enter a value "))
num3 = float(input("Enter a value "))
num4 = float(input("Enter a value "))

product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4)/4
#Display values with f-string
#Display the product and the average with 0 decimal places
print(f'{product:.0f} {average:.0f}')

#Display the product in average with 3 decimal places
print(f'{product:.3f} {average:.3f}')
