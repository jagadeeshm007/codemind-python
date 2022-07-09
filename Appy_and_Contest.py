x=int(input())
for i in range(x):
    n,a,b,k=map(int,input().split())
    h=n//a
    s=n//b
    if(h+s>=k):
        print("Win")
    else:
            print("Lose")