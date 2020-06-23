n=int(input())
x=list(map(int,input().split()))
w=list(map(int,input().split()))
sum=0
sum1=0
for i in w:
    sum+=i
for i in range(n):
    sum1+=x[i]*w[i]
mean=sum1/sum
print('%.1f'%mean)
