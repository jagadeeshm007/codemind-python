n=input()
n.lower()
c=0
k=-1
for i in range(len(n)):
    c=0
    for j in range(len(n)):
        if i!=j:
            if n[i]==n[j]:
                c=1
                break
    if c==0:
        k=i
        break
if k==-1:
    print("-1")
else:
    print(k)