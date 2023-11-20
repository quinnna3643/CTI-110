#Allison Quinn
#11/20/23
#using if/else statements

#Get the input from the user

name = input('Enter the employee name: ')
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
print('Employee name:', name)
print('pay per hour:', pay)
print('Totals hours worked:', hours)
print('overtime hours worked:', overtime)
print('amount payed for overtime:', otpay)
print('regular hours worked:', reg_hours)
print('amount payed for regular hours:', regpay)
print('the total amount payed to the employee is:', otpay + regpay)

            
