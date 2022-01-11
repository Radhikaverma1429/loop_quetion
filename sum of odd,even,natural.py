#num=int(input("enter a number = "))
# sum=0
# i=1
# while i<=100:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
#     print(sum,"even")
#     if i%2!=0:
#         sum+sum+i
#     i+i+1
#     print(sum,"odd")
# else: 
#         sum=sum+i
# i=i+1
# print(sum,"natural")
    
count=0
count2=0
i=1
while i<=100:
    if i%2==0:
        count=i
    elif i%2!=0:
        count2=i
    else:
        print("natural")
    i=i+1
print(count,"total of even number: ")
print(count2,"total of odd number: ")