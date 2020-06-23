n=int(input())
x=list(map(int,input().split()))
x.sort()
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
wm=calcmedian(x)
l=[]
u=[]
for i in x:
    if (i<wm):
        l.append(i)
    elif(i>wm):
        u.append(i)
print(int(calcmedian(l)))
print(int(wm))
print(int(calcmedian(u)))
