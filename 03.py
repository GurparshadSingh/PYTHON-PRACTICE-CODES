# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
def compute(n,m):
    value = n+n*n+n*n*n
    return value
print("value of given expreiion in given problem is:",compute(1,1))