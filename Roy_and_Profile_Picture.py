l=int(input())
t=int(input())
while t:
    w,h=map(int,input().split())
    ##print(w,h)
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w>=l and h>=l:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")
    t-=1