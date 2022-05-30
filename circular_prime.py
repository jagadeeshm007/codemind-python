def prime(c):
    if c<2:
        return 0
    else:
        for i in range(2,int(c**0.5)+1):
            if c%i==0:
                return 0
        return 1
def rev(a):
    t=k=0
    while a:
        t=a%10
        k=(k*10)+t
        a=a//10
    return k
n=int(input())
k=rev(n)
if  prime(n)!=1:
    print("not prime")
else:
    if prime(n)==1 and prime(k)!=1:
        print("prime but not a circular prime")
    elif prime(n)==1 and prime(k)==1:
        print("circular prime")