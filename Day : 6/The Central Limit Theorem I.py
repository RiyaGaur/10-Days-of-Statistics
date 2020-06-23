import math

x = int(input())
n = int(input())
m = int(input())
s = int(input())

mu_sum = n * m 
sigma_sum = math.sqrt(n) * s

def cdf(x, m, s):
    Z = (x - m)/s
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))
