#Allison Quinn

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total/len(grades)

print(f'The lowest grade is {low:.2f}')
print(f'The highest grade is {high:.2f}')
print(f'The sum grade is {total:.2f}')
print(f'The average grade is {avg:.2f}')
