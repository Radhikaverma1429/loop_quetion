r=1
while r<=5:
    c=1
    while c<=42:
        if (r==1 and (c==4 or c==5 or c==7 or c==9 or c==10 or c==12 or c==13 or c==15 or c==16 or c==20 or c==24 or c==28 or c==29 or c==33 or c==34 or c==38 or c==40 or c==41)):
            print(" ",end=" ")
        elif (r==2 and (c==1 or c==3 or c==4 or c==6 or c==8 or c==10 or c==12 or c==13 or c==15 or c==17 or c==18 or c==19 or c==20 or c==21 or c==23 or c==24 or c==26 or c==27 or c==29 or c==31 or c==32 or c==34 or c==35 or c==37 or c==38 or c==40 or c==42)):
            print(" ",end=" ")
        elif (r==3 and(c==1 or c==3 or c==4 or c==6 or c==7 or c==8 or c==10 or c==12 or c==13 or c==15 or c==16 or c==19 or c==20 or c==21 or c==23 or c==24 or c==26 or c==27 or c==29 or c==31 or c==32 or c==34 or c==35 or c==37 or c==38 or c==41 or c==42)):
            print(" ",end=" ")
        elif (r==4 and(c==1 or c==3 or c==4 or c==5 or c==7 or c==9 or c==10 or c==12 or c==13 or c==15 or c==16 or c==17 or c==18 or c==20 or c==21 or c==23 or c==24 or c==26 or c==27 or c==29 or c==31 or c==32 or c==34 or c==35 or c==37 or c==38 or c==40 or c==42)):
            print(" ",end=" ")
        elif (r==5 and(c==4 or c==5 or c==6 or c==8 or c==9 or c==10 or c==11 or c==14 or c==15 or c==19 or c==20 or c==24 or c==28 or c==29 or c==33 or c==34 or c==38 or c==40 or c==41)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        c=c+1
    print( )
    r=r+1