#Allison Quinn
#10/19/23
#Working with nested if/else statements

#Create a boolean variable to hold leap year status
is_leap = False

#Get year from user
year = int(input('Enter a year to determine if its a leap year: '))


if year % 4 == 0:               #Does year divide by 4
    if year % 100 == 0:         #Does year divide by 100
        if year % 400 == 0:     #Does year divide by 400
            is_leap = True
        else:
            is_leap = False     #Does NOT divide by 400
    else:
        is_leap = True          #Does NOT divide by 100
else:
    is_leap = False             #Does NOT divide by 4

#Print output to user
if is_leap == True:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is NOT a leap year")
