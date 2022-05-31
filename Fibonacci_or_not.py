n=int(input())
##print(n)
k=s=0
d=1
for i in range(n):
    k=s+d
    if k==n:
        print("True")
        break
    if k>n:
        print("False")
        break
    ##print(k)
    s=d
    d=k