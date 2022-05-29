n=int(input())
s=d=0
p=1
while n:
    s=n%10
    p=p*s
    d=d+s
    n=n//10
print(p-d)
