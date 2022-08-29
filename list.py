# l=[12, 35, 9, 56, 24]
# size=len(l)
# tem=l[0]
# l[0]=l[size-1]
# l[size-1]=tem 
# print(l)

# l=[1,2,3,4,5,6,7]
# a=len(l)
# print(a)

# l=[1,2,3,4,5,6,7]
# i=0
# c=0
# while i<len(l):
#     c+=1
#     i+=1 
# print(c) 

# l=[1,2,3,4,5,6,7]
# print(len(l))


# l=[1,2,3,4,5,6,7]
# i=0 
# num=int(input("enter a number "))
# while i<len(l):
#     if num in l:
#         print("exists")
#     else:
#         print("not exists")
#     i+=1

# l=[1,2,3,4,5,6,7]
# l.clear()
# print(l)  

# without using clear method to deleat list
# list1 = [1,2,3,4,5,6,7] 
# list1=list1*0
# print (list1)       


#without using reverse methode to revers the list
# l=[1,2,3,4,5,6,7]
# n=l[::-1]
# print(n) 


# l=[1,2,3,4,5,6,7]
# sum=0
# i=0
# while i<len(l):
#     sum+=i
#     i+=1
# print(sum)  


# l=[1,2,3,4,5,6,7]
# sum=1
# i=0 
# while i<len(l):
#     sum=sum*l[i]
#     i+=1
# print(sum) 

# l=[1,2,3,4,5,6,7]
# m=l[0]
# i=0
# while i<len(l):
#     if l[i]<m:
#         m=l[i]
#     i+=1
# print(m) 

# l=[1,2,3,4,5,6,7]
# m=0
# i=0
# while i<len(l):
#     if l[i]>m:
#         m=l[i]
#     i+=1
# print(m)

# l=[1,2,3,4,5,6,7]
# i=0
# while i<len(l):
#     if i%2==0:
#         print(i,"even")
#     i+=1

# l=[1,2,3,4,5,6,7]
# i=0
# while i<len(l):
#     if i%2!=0:
#         print(i,"odd")
#     i+=1

# i=1
# while i<=20:
#     if i%2==0:
#         print(i,'even no')
#     i+=1


# i=1
# while i<=20:
#     if i%2!=0:
#         print(i,'even no')
#     i+=1

# l = [11, -21, 0, 45, 66, -93]
# i=0
# while i<len(l):
#     if l[i]>0:
#         print(l[i])
#     i+=1

# l = [11, -21, 0, 45, 66, -93]
# i=0
# while i<len(l):
#     if l[i]<0:
#         print(l[i])
#     i+=1

# i=-5
# while i<=10:
#     if i>0:
#         print(i)
#     i+=1

# i=-5
# while i<=10:
#     if i<0:
#         print(i)
#     i+=1

# test_list = [5, 6, [], 3, [], [], 9]
# i=0
# l=[]
# while i<len(test_list):
#     if test_list[i]!=[]:
#         l.append(test_list[i])
#     i+=1
# print(l) 

# li1 = [4, 8, 2, 10, 15, 18]
# li_copy = li1[:]
# print(li_copy)
# print(li1)

# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# l=20
# i=0
# c=0
# while i<len(lst):
#     if lst[i]==l:
#         c+=1
#     i+=1
# print(c) 

# l=[(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
# i=0
# a=[]
# while i<len(l):
#     if l[i]!=() and l[i]!=('',''):
#         a.append(l[i])
#     i+=1
# print(a) 

# list1 = [10, 20, 30, 20, 20, 30, 40,50, -20, 60, 60, -20, -20]
# i=0
# l=[]


# list=[10,20,30,40,50]
# sum=0
# i=0
# l=[]
# while i<len(list):
#     sum=sum+list[i]
#     l.append(sum)
#     i+=1
# print(l)