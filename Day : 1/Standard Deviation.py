import math
n=int(input())
t=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=t[i]
    mode=sum/n
ss=0
for i in t:
    ss+=(i-mode)**2
d=math.sqrt(ss/n)
print('%.1f'%d)
