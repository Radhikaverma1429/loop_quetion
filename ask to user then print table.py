n=int(input("enter a number ="))
i=1
while i<=n:
    j=1
    while j<=10:
        print(i,"*",j,"=",(j*i))
        j+=1
    print( )
    i=i+1 