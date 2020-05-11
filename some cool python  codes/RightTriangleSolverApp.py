#triangle solver ap
import math

print("Welcome to the Right Triangle Solver App")

base = float(input("What is the base of the triangle: "))
height = float(input("What is the height of the triangle: "))

hypo = math.sqrt((base**2) + (height**2))

area = (1/2) * (base * height)

hypo = round(hypo, 3)
area = round(area, 3)
base = round(base, 3)
height = round(height, 3)

# print("For a triangle with base " + str(base) + " and " + str)

print("\nFor a triangle with base {} and height {} the hypoteuse is {}.".format(base, height, hypo))
print("For a trianlgle with dimenstion base {} and height {} the area is {}.".format(base, height, area))
