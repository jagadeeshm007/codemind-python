n=int(input())
k=n
t=e=0
while k:
    t=k%10
    e=(e*10)+t
    k=k//10
if e==n:
    print("True")
else:
    print("False")