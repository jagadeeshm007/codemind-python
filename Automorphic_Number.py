def rev(z):
    t=k=0
    while z:
        t=z%10
        k=(k*10)+t
        z=z//10
    return k
n=int(input())
m=p=n*n
z=n
t=k=0
while z:
    t=z%10
    k+=1
    z=z//10
t=u=0
while k:
   t=p%10
   u=(u*10)+t
   p=p//10
   k-=1
j=rev(u)
if j==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")