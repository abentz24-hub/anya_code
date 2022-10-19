#root.py

#define variables
a = 1
b = 1
c = -6

#calculate the values of x
first_x = (b + (b**2 - 4*a*c)**(.5)) /(2*a)
second_x = (-b - (b**2 - 4*a*c)**(.5)) /(2*a)

#output results to the screen
print(first_x)
print(second_x)
print("Solutions:",first_x,"and", second_x)