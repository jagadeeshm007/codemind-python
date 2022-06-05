t=int(input())
while t:
    n=input()
    c=0
    for i in n:
        if i.isdigit():
            c=1
            break
    if c==0:
        print("No")
    else:
        print("Yes")
    t-=1