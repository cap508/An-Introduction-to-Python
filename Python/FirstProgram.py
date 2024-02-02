import math

# This program calculates the roots ofa quadratic
# i.e. (-b +/- math.sqrt (b^2 - 4ac))/2a

a = 1.0
b = 1.0
c = -6.0

root1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2*a)
root2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2*a)

print(f"The roots are {root1}, {root2}")