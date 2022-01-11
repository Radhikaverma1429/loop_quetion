a=[1,4,6,3,5,8,10,2,7,9]
i=0
empty=[]
while i<len(a):
    j=-1
    while j>-(a[i]):
        if a[i]>a[j+1]:
            a[j]=a[i]
            empty.append(a[j])
        j-=1
    i+=1
print(empty)