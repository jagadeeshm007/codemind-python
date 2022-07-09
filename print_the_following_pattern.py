x=int(input())
asciichr=65
for i in range(x,0,-1):
    for j in range(i):
        print(chr(asciichr+x-1),end=' ')
    asciichr-=1
    print()
        