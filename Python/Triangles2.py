import math

side1 = float(input("Length of side one : "))
side2 = float(input("Length of side two : "))
angle = float(input("Angle (degrees) between the two lines : ")) * math.pi/180

print(f"The length of side 3 is {math.sqrt(side1**2 + side2**2 - 2*side1*side2*math.cos(angle))}")

