t=int(input())
m=int(input())
s=0
for i in range(t,m+1):
    f=0
    n=i
    if n<10:
        f=0
    else:
        while n:
            s=n%10
            if s!=0:
                if i%s!=0:
                    ##print(i,s)
                    f=1
                    break
            else:
                f=1
                break
            n=n//10
    ##print(f,"s")
    if f==0:
        print(i,end=" ")