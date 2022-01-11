i=0
value=0
avrage=0
while i<=11:
    num=int(input("enter a number:",))
    value=value+num
    i=i+1
avrage=value/11
print(avrage)
if avrage%5==0:
    print("it't divisible by 5=",avrage)
else:
    print("is't not divisible 5")