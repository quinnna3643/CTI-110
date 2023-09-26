# Your Name
# Date
# calculates travel expenses

budget = int(input("Enter Budget: "))

dest = input("where are you traveling? ")

gas = int(input("Enter gas budget: "))
food = int(input("Enter food budget: "))
hotel = int(input("Enter hotel budget: "))

expenses = gas+food+hotel

print("-------------Travel Expenses---------")
print("Location: ", dest)
print("Initial Budget: ", budget)
print()
print("Gas Cost: ", gas)
print("Gas Food: ", food)
print("Gas Hotel: ", hotel)
print()
print("Remaining Balance: ", budget-expenses)
