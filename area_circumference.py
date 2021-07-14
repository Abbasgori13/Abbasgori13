import math
pi = math.pi

r = float(input("Enter the radius :"))

area = pi * (r ** 2)
circumference = 2 * pi * r

print("Your Area for given radius ", r , "=" , round(area,3) )
print("Your Circumference for given radius ", r , "=" , round(circumference,3) )