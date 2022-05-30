def sum(n):
    k=0
    for i in range(1,n):
        if n%i==0:
            k=k+i
    return k
a=int(input())
b=int(input())
n=sum(a)
m=sum(b)
if a==m and b==n:
    print("Amicable")
else:
    print("Not Amicable")