# Python Program to Find the Factorial of a Number

num = int(input("enter your number"))
def factCalc(num):
    if num==0 or num==1:
        return 1
    else:
        factorial = num*factCalc(num-1)
        return factorial
print(factCalc(num))
        