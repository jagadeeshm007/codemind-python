n=input()
s=0
for i in n:
    if i.isdigit():
        s=s+(ord(i)-48)
print(s)