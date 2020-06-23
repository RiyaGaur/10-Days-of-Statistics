import math
import collections
n=int(input())
t=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=t[i]
    mode=sum/n
print(mode)
n = len(t) 
t.sort()
if n % 2 == 0: 
    median1 = t[n//2] 
    median2 = t[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = t[n//2] 
print(median)
occurrences = collections.Counter(t)
max = max(occurrences.keys(), key=(lambda k: occurrences[k]))
print(max)
