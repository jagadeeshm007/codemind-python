def nonp(a):
    c=0
    if a==1:
        c=1
    for i in range(2,a):
        if a%i==0:
            c=1
            break
    if c==1:
        return 1
    else:
        return 0
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if nonp(i)==1:
            c+=1
print(c)