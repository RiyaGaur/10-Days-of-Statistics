from math import factorial, exp
n=float(input())
x=int(input())
a=n**x
b=exp(-n)
pp=(a*b)/factorial(x)
print("%.3f" %pp)
