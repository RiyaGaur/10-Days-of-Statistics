p=1/3 q=1-p

n=1

k=0

for i in range(5):

j=pow(q,n-1)

l=j*p

k=k+l

n=n+1

print(round(k,3))
