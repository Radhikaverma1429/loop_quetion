r=0
while r<=5:
    c=0
    while c<=4:
        if (r==0 or c==2) or r==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print( )
    r=r+1

# r=1
# while r<=5:
#     c=1
#     while c<=3:
#         if (r==2) and (c==1 or c==3)or(r==3) and (c==1 or c==3)or(r==4) and (c==1 or c==3):
#             print(" ",end=" ") 
#         else:
#             print("*",end=" ")
#         c=c+1
#     print( )
#     r=r+1

