a=int(input()) 
s=0
for i in range(1,a+1):
    s=s+float(1/i)
print("{0:.2f}".format(s))