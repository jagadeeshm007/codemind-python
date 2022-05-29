n=int(input())
c=65
for i in range(n):
    for j in range(n):
        print(chr(c+i),end=" ")
    print()