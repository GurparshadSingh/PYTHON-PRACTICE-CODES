# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
a = int(input("enter 1st number"))
b= int(input("enter 2nd number"))
c = int(input("enter 3rd number"))

def calcSum(a,b,c):
    if a==b==c:
        return 3*(a+b+c)
    else:
        return a+b+c
print(calcSum(a,b,c))
