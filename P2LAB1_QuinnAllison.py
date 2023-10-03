#Allison Quinn
#10/3/2023
#Use floas and expressions to calculate gas cost

#Create input variables
mpg = float(input("Enter the car's mpg: "))
cost_per_gallon = float(input("How much does a gallon of gas cost: "))

#Calcualte gas cost based off gallons needed & price per gallon
#Calcualte for 20 miles, 75miles, & 500miles

cost_20 = (20/mpg) * cost_per_gallon
cost_75 = (75/mpg) * cost_per_gallon
cost_500 = (500/mpg) * cost_per_gallon

#Output are values using an f-string and format the floats
print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")
