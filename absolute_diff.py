# Write a Python program to test whether a number is within 100 of 1000 or 2000
num =int(input("Enter a number"))

if abs(num-1000)<=100 or abs(num-2000)<=100:
    print(f"The number {num} lies between the given range 100 of 1000 or 2000")
else:
    print("It does not lie in the range")