def check(a):
    if a%2==0:
        return 0
    else:
        return 1
a=int(input())
k=c=0
while a:
    t=a%10
    if check(t)==1:
        c+=1
    else:
        k+=1
    a=a//10
if c==0 and k>0:
    print("Even")
elif c>0 and k==0:
    print("Odd")
else:
    print("Mixed")