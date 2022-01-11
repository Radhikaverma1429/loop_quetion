r=0
while r<=4:
    c=0
    while c<=4:
        if (c==1 or c==2 or c==3) and (r!=1 and r!=2 and r!=3) or (c==0) and (r!=0 and r!=4):
            print("*",end=" ")
        else:
            print(end="  ")
        c=c+1
    print( )
    r=r+1