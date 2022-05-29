n=int(input())
if n>=3 and n<=100:
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(n-1,-1,-1):
        for j in range(i):
            print("*",end="")
        if i>0:
            print()
else:
    print("The pattern is not possible")