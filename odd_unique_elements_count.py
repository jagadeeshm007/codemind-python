n=int(input())
a=list(map(int,input().split()))
c=0
k=set(a)
for i in k:
    if i%2!=0:
        c+=1
print(c)