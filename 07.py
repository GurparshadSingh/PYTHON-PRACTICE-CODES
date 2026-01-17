# Python Program to Calculate the Area and Perimeter of Triangle and Circle.
import math
def area_and_peri_of_circle(a):
    ar = math.pi*(pow(a,2))
    pe = 2*math.pi*a
    area = round(ar,2)
    peri = round(pe,2)
    return area,peri

value_cir = area_and_peri_of_circle(1)
print("The area and perimeter of circle resp. are :",value_cir)

def area_and_peri_of_triangle(x,y,z):
    area = 1/2*x*y
    peri = x+y+z
    return area,peri

value_triangle = area_and_peri_of_triangle(1,1,1)
print("The area and perimeter of triangle resp. are :",value_triangle)