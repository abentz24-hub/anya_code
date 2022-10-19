#penny.py
#user input
pennies = input("How many pennies do I have") 
pennies = int(pennies)
#calcualte
nickels = pennies // 5
new_pennies = pennies % 5
#print statement
print(pennies,"pennies can be converted into", nickels, "nickels and", new_pennies,"pennies")