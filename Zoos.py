n=input()
z=o=0
for i in n:
    if i=="z":
        z+=1
    if i=="o":
        o+=1
if z*2==o:
    print("Yes")
else:
    print("No")