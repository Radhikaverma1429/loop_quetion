r=1
while r<=5:
    c=1
    while c<=3:
        if (r==2) and (c==2 or c==3)or(r==4) and (c==2 or c==3):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        c=c+1
    print( )
    r=r+1 