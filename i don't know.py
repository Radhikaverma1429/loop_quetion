num1=int(input("enter a number "))
num2=int(input("enter a number "))
while num1<=num2:
    i=1
    f=0
    while i<=num1:
        if num1%i==0:
            f=f+1
        i=i+1
    if num1==2:
        num1+=1
    print(num1) 