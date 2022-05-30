n=int(input())
k=0
for i in range(n):
    if i*(i+1)==n:
        print("YES")
        break
    if i*(i+1)>n:
        print("NO")
        break