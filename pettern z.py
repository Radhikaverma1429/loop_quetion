r=1
while r<=5:
    c=1
    while c<=5:
        if (r==2) and (c==1 or c==2 or c==3 or c==5):
            print(" ",end=" ")
        elif (r==3) and (c==1 or c==2 or c==4 or c==5):
            print(" ",end=" ")
        elif (r==4) and (c==1 or c==3 or c==4 or c==5):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        c+=1
    print( )
    r+=1

