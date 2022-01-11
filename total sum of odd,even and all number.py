num=int(input("enter a number = "))
i=1
sum=0
even=0
odd=0
while i<=num:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
    sum=sum+i
    i=i+1
print("total even:",even)
print("total odd:",odd)
print('total sum:',sum) 