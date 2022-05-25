n,m=map(int,input().split())
d=n
c=z=0
while d:
    d=d//10
    c+=1
k=c-m
z=10**k
s=n//z
s1=n%(10**m)
print(abs(s-s1))