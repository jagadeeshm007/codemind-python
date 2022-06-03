n=int(input())
a=list(map(int,input().split()))
s=int(input())
flag=0
for i in range(n):
    if s==a[i]:
        print(i)
        flag=1
if flag==0:
    print("-1")