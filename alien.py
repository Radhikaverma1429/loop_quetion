r=1
while r<=5:
    c=1
    while c<=27:
        if (r==1 and(c==1 or c==5 or c==9 or c==13 or c==14 or c==18 or c==19 or c==23 or c==25 or c==26)):
            print(" ",end=" ")
        elif (r==2 and(c==2 or c==3 or c==4 or c==5 or c==6 or c==8 or c==9 or c==11 or c==12 or c==14 or c==16 or c==17 or c==19 or c==20 or c==22 or c==23 or c==25 or c==27)):
            print(" ",end=" ")
        elif (r==3 and(c==1 or c==4 or c==5 or c==6 or c==8 or c==9 or c==11 or c==12 or c==14 or c==16 or c==17 or c==19 or c==20 or c==22 or c==23 or c==26 or c==27)):
            print(" ",end=" ")
        elif (r==4 and(c==1 or c==2 or c==3 or c==5 or c==6 or c==8 or c==9 or c==11 or c==12 or c==14 or c==16 or c==17 or c==19 or c==20 or c==22 or c==23 or c==25 or c==27)):
            print(" ",end=" ")
        elif (r==5 and(c==4 or c==5 or c==9 or c==13 or c==14 or c==18 or c==19 or c==23 or c==25 or c==26)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        c=c+1
    print( )
    r=r+1