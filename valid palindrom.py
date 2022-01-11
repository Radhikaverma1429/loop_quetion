s = "A man, a plan, a canal: Panama"
b=""
i=-1
while i>=-len(s):
    b=b+s[i]
    i-=1    
    s=s.replace(",","")
    s=s.replace(" ","")
    s=s.replace(":","")
    b=b+s[i]
    i-=1
if s==b:
    print("ture")
else:
    print("false")
print(s) 

