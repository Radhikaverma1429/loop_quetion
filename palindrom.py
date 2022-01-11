n=int(input("enter a number :"))
a=n
rev=0
i=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if a==rev: 
    print("palindrome","true") 
else:
    print("not palindrome","false")    
i+=1
