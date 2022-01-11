a=[10,11,12,13,14,17,18,19]
num=30
i=0
empty=[]
while i<len(a):
    j=i
    empty1=[]
    while j<len(a):
        if a[i]+a[j]==num:
            empty1.append(a[i])
            empty1.append(a[j])
            empty.append(empty1)
        j+=1
    i+=1
print(empty) 


