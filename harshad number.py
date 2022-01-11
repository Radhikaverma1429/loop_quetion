# num=int(input("enter a number "))
# n=num
# sum=0
# while num>0:
#     rev=num%10
#     sum=sum+rev
#     num=num//10
# if(n%sum == 0):    
#     print(str(n) + " is a harshad number")   
# else:    
#     print(str(n) + " is not a harshad number")


num=[8,5,76,54]
n=len(num)
empty=[]
sum=0
while len(num)>0:
    rev=len(num)%10
    sum=sum+rev
    n=n//10
if n%sum==0:
    print("harshad number") 
    empty.append(sum)

