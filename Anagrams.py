x=input()
y=input()
x=x.lower()
y=y.lower()
x=sorted(x)
y=sorted(y)
if x==y:
    print("True")
else:
    print("False")