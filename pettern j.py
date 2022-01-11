r=1
while r<=4:
    c=1
    while c<=3:
        if (r==2 and (c==1 or c==3)) or (r==3 and (c==1 or c==3)) or (r==4 and (c==4)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        c=c+1
    print( )
    r+=1
    