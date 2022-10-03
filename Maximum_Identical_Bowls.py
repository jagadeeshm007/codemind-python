n=int(input())
a=list(map(int,input().split()))
k=sum(a)
z=n
for i in range(z,0,-1):
    #print(k,z,k%z,k//z)
    if k%z==0:
        print(z)
        break
    z-=1