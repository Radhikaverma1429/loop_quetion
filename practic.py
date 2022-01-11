n=7
r=4
while r>=0:
    c=1
    while c<=5:
        print(" ",end=" ")
        c=c-1
    i=1
    while i<=r:
        print(str(n)*n)
        i=i+1
        n=n-2
    print( )
    r=r+1