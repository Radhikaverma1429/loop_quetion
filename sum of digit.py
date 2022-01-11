i=int(input("enter a digit:"))
sum=0
while i>0: 
    digit=i%10
    i=i//10
    print(digit)
    sum=sum+digit
print(sum) 