a=int(input())
##print(a)
for i in range(1,a+1):
    if a%2==0:
        a=a//2
        ##print(a)
    elif a%3==0:
        a=a//3
       ## print(a)
    elif a%5==0:
        a=a//5
        ##print(a)
    else:
        break;
##print(a)
if a==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")