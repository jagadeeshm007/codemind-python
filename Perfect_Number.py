t=int(input())
s=0
for i in range(1,t):
    if t%i==0:
        s=s+i
if s==t:
    print("True")
else:
    print("False")