import math
x = 250
n = 100
s_mean = 2.4
s_stdev = 2.0
stdev = s_stdev * math.sqrt(n)

cdf = 0.5 * (1 + math.erf((x - s_mean * n) / (stdev * math.sqrt(2))))

print(round(cdf,4))
