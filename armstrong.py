num=int(input("enter a number :"))
sum=0
n=num
a=str(num)
while n>0:
    digit=n%10
    sum=sum+digit**len(a)  
    n=n//10
if sum==num:
    print(num,"is armstrong")
else:
    print(num,"is not arm