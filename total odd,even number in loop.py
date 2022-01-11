i=1
c=0
c1=0
while i<=5:
    num=int(input("enter a number = "))
    if num%2==0:
        c=c+1
    else:
        c1=c1+1
    i=i+1
print(c)
print(c1)