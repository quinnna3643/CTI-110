#Allison Quinn
#11/20/23
#using if/else statements
numemployee = 0
totalot = 0
totalreg = 0
totalgross = 0

#Get the input from the user

name = input('Enter the employee name: ')
#The loop starts here
while name != 'Done':
    numemployee += 1
    hours = int(input('Enter the employees hours: '))
    pay = float(input('How much does the employee make per hour: '))

    if hours > 40:
        overtime = hours - 40
        reg_hours = 40
        otpay = (pay * 1.5) * overtime
        regpay = reg_hours * pay
    else:
        overtime = 0
        reg_hours = hours
        otpay = 0
        regpay = reg_hours * pay
    totalot += otpay
    totalreg += regpay
    totalgross += (regpay + otpay)
    print('Employee name:', name)
    print('pay per hour:', pay)
    print('Totals hours worked:', hours)
    print('overtime hours worked:', overtime)
    print('amount payed for overtime:', otpay)
    print('regular hours worked:', reg_hours)
    print('amount payed for regular hours:', regpay)
    print('the total amount payed to the employee is:', otpay + regpay)
    name = input('Enter the employee name: ')
#loop has ended display information
print('Total number of employees:', numemployee)
print(f'Total amount paid for overtime: ${totalot:.2f}')
print(f'Total amount paid for regular hours: ${totalreg:.2f}')
print(f'Total amount paid in gross: ${totalgross:.2f}')



            
