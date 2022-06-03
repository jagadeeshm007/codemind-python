n=int(input())
a=list(map(int,input().split()))
m=int(input())
z=0
d=[]
for i in range(n):
    if a[i]==m:
        z=1
        d.append(i)
if z==1:
    print(d[0],d[(len(d))-1])
else:
    print("-1 -1")
    