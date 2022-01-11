r=1
while r<=5:
    c=1
    while c<=4:
        if (r==1 and(c==2 or c==3))or(r==2 and(c==2 or c==3))or(r==3 and(c==2 or c==3))or(r==4 and(c==2 or c==3))or(r==5 and(c==1 or c==4)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        c=c+1
    print( )
    r=r+1