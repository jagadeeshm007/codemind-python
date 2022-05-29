n=int(input())
s=n*n
d=f=0
while s:
    d=s%10
    f=f+d
    s=s//10
if f==n:
    print("Neon Number")
else:
    print("Not Neon Number")