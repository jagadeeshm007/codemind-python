n=int(input())
k=n
a=[0]*n
i=s=0
while k:
    b=int(input())
    a[i]=b
    i+=1
    k-=1
t=int(input())
for i in range(n):
    if a[i]>t:
        s+=2
    if a[i]<=t:
        s+=1
print(s)