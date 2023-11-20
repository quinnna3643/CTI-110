#Allison Quinn
#10/19/23
#Working with nested if/else statements

def divide_by_4(myyear):
    if myyear % 4 == 0:
        return True
    else:
        return False

def divide_by_100(myyear):
    if myyear % 100 == 0:
        return True
    else:
        return False

def divide_by_400(myyear):
    if myyear % 400 == 0:
        return True
    else:
        return False

def print_output(is_leap, year):
    if is_leap == True:
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is NOT a leap year")

def main():
    #Create a boolean variable to hold leap year status
    is_leap = False

    #Get year from user
    year = int(input('Enter a year to determine if its a leap year: '))


    if divide_by_4(year):                                #Does year divide by 4
        if divide_by_100(year):         #Does year divide by 100
            if divide_by_400(year):    #Does year divide by 400
                is_leap = True
            else:
                is_leap = False     #Does NOT divide by 400
        else:
            is_leap = True          #Does NOT divide by 100
    else:
        is_leap = False             #Does NOT divide by 4

    #Print output to user
    print_output(is_leap, year)

#call the main function
if __name__ == '__main__':
    main()
