# st = input("enter a palindrome! ")
# j = -1
# flag = 0
# for i in st:
#     if i != st[j]:
#         flag = 1
#         break
#     j = j - 1
# if flag == 1:
#     print("NO")
# else:
#     print("Yes")

# string = 'amaama'
# half = int(len(string) / 2)
 
# if len(string) % 2 == 0:
#     first_str = string[:half]
#     second_str = string[half:]
# else: 
#     first_str = string[:half]
#     second_str = string[half+1:]
# if first_str == second_str:
#     print(string, 'string is symmertical')
# else:
#     print(string, 'string is not symmertical')
# if first_str == second_str[::-1]:
#     print(string, 'string is palindrome')
# else:
#     print(string, 'string is not palindrome') 

# str1= 'geeks quiz practice code'
# str1=str1[::-1]
# print(str1)

# test_str = "GeeksForGeeks"
# print ("The original string is : " + test_str)
# new_str = ""
# for i in range(len(test_str)):
#     if i != 2 and i!=3 and i!=4:
#         new_str = new_str + test_str[i]
# print ("The string after removal of i'th character : " + new_str) 

# test_str = "GeeksForGeeks"
# print (test_str)
# new_str = test_str[:3] +  test_str[6:] 
# print (new_str) 

# MyString1 =input("enter a substring")
# MyString2 =input("enter a substring is their or not ")
# c=0
# if MyString2 in MyString1:
#     c+=1
#     print(c)
#     print("yes")
# else:
#     print("no") 


# try after some time 

test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
# {'Gfg': 2, 'is': 1, 'best': 1, '.': 1, 'Geeks': 2, 
# 'are': 1, 'good': 1, 'and': 1, 'like': 1}
s=test_str.split()
print(s)
d={} 
c=0
i=0
while i<len(s):
    c=c+1
    d[i]=c 
print(d)  

# str = "geeks"
# c=0
# for i in str:
#     c+=1
# print(c) 

# s = "i am muskan"
# l=list(s)
# i=0
# while i<len(l):
#     if i%2==0:
#         print(i)
#     i+=1

# ip1 = "geeks"
# ip2 = "geeksonly"
# i=0
# c=0
# while i<len(ip1):
#     if ip2[i] in ip1[i]:
#         c+=1
#     i+=1
# print(c) 




 
