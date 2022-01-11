# num=int(input("enter a number:-"))
# i=1
# c=0
# while i<=num:
#     if num%i==0:
#         c=c+1
#     i=i+1
# if c==2:
#     print(num,"is prime number")
# else:
#     print(num,"is not prime num")

# num=int(input("enter a number"))
i=1
while i<=100:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        print(i,"is prime")
    i=i+1 