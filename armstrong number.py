i=int(input("enter a armstrong number = "))
ori=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if ori==sum:
    print(sum,"is armstorng number")
else:
    print(sum,"is not armstrong number")

