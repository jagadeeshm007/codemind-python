n=int(input())
a=input()
k=list(a.strip(" "))
j=[]
for i in k:
    if i!=" ":
        j.append(int(i))
print(sum(j))