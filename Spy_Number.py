n=int(input())
k=m=0
s=1
e=n
while e:
    k=e%10
    m=m+k
    s=s*k
    e=e//10
if s==m:
    print("Spy Number")
else:
    print("Not Spy Number")