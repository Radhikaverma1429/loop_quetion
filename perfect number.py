num=int(input("enter a number ="))
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")