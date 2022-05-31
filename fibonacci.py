n=int(input())
s=k=0
m=1
print("0 1",end=" ")
for i in range(n-2):
    k=s+m
    print(k,end=" ")
    s=m
    m=k