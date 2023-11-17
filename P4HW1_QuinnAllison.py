#Allison Quinn
#11/17/23
#
from statistics import mean

num_scores = int(input('Enter the number of scores'))
scorelist = []
for scores in range(num_scores):
    grade = int(input(f'Enter grade #{scores + 1}: '))
    while grade < 0 or grade > 100:
        print('You entered an invalid grade try again')
        grade = int(input(f'Enter grade #{scores + 1}: '))
    scorelist.append(grade)

print('---------Results---------')
minu = min(scorelist)
print('Lowest Score :', minu)
newlist = scorelist.remove(minu)
print('Modified List :', newlist)

average = sum(newlist)/len(newlist)
print('Scores Average :', average)

if average <= 100 and average >= 90:
    letter = "A"
elif average <= 89 and average >= 80:
    letter = "B"
elif average <= 79 and average >= 70:
    letter = "C"
elif average <= 69 and average >= 60:
    letter = "D"        
else:
    letter = "F"
                        
                        
    
            
