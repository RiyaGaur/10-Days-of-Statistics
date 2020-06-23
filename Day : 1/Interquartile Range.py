n=int(input())
x=list(map(int,input().split()))
f=list(map(int,input().split()))
s = []
for i in range(n):
    s += [x[i]] * f[i]
N = sum(f)
s.sort()
a=[]
def calcmedian(a):
    n = len(a) 
    if n % 2 == 0: 
        median1 = a[n//2] 
        median2 = a[n//2 - 1] 
        median = (median1 + median2)/2
    else: 
        median = a[n//2] 
    return median
if n%2 != 0:
    q1 = calcmedian(s[:N//2])
    q3 = calcmedian(s[N//2+1:])
else:
    q1 = calcmedian(s[:N//2])
    q3 = calcmedian(s[N//2:])
q=q3-q1
print('%.1f'%q)
