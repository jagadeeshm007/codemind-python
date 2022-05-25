n,m=map(int,input().split())
for i in range(1,m+1):
    if(i%2)==1:
        print("%d x %d = %d"%(n,i,i*n))