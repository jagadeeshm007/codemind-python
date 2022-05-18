def prime(a):
    c=0
    if a==1:
        c=1
    else:
        for i in range(2,a):
            if(a%i)==0:
                c=1
                break
    if c==0:
        return 0
    else:
        return 1
def rev(a):
    d=a
    i=s=0
    while a:
        s=a%10
        i=(i*10)+s
        a=a//10
    if i==d:
        return 0
    else:
        return 1
   
n=int(input())
n=n+1
test=1
while test:
    if rev(n)==0:
        if prime(n)==0:
            test=0
            break
        else:
            n+=1
    else:
        n+=1
print(n)
    
    
    