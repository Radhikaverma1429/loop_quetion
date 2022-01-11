# n=1
# raw=1
# while raw<=4:
#     c=1
#     while c<=raw:
#         print(n,end=" ")
#         n=n+1
#         c+=1
#     print()    
#     raw=raw+1

a=int(input("enter a number "))
i=0
while i<a:
	j=0
	c=" "
	d=str(a[i])
	while j<len(d):
		if d[j]=='0':
			c=c+'zero'
		elif d[j]=='1':
			c=c+'one'
		elif d[j]=='2':
			c=c+'two'
		elif d[i]=='3':
			c=c+'three'
		j+=1
	i=i+1
	# b.append(c)
print(c)