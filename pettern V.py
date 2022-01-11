r=1
while r<=4:
    c=1
    while c<=7:
        if (r==1 and(c==2 or c==3 or c==4 or c==5 or c==6))or(r==2 and(c==1 or c==3 or c==4 or c==5 or c==7))or(r==3 and(c==1 or c==2 or c==4 or c==6 or c==7))or(r==4 and(c==1 or c==2 or c==3 or c==5 or c==6 or c==7)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        c=c+1
    print( )
    r=r+1