r=1
while r<=3:
    c=1
    while c<=3:
        if c==1 or c==3 or c==2 and r==2:
            print("*",end=" ")
        else:
            print(end="  ")
        c=c+1
    print( )
    r=r+1
    