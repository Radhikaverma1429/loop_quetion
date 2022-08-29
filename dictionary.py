# dict = {'a': 100, 'b':200, 'c':300}
# sum=0
# for i in dict:
#     sum=sum+dict[i]
# print(sum) 

# test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
# # test=test_dict.pop('Mani')
# d={}
# for i in test_dict:
#     for j in (i): 
#         if i!="Mani":
#             d["new"]=test_dict[i]
# print(d) 

# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict3 = {}
# dict3.update(dict1)
# dict3.update(dict2)
# print(dict3)

# test_dict = {'month' : [1, 2, 3],'name' : ['Jan', 'Feb', 'March']}
# a=test_dict.get('month')
# b=test_dict.get('name')
# dic={}
# for i in range(len(a)):
#     dic[a[i]]=b[i]
# print(dic)

# votes =['john','johnny','jackie','johnny','john','jackie',
#     'jamie','jamie','john','johnny','jamie','johnny','john']

def pattern(n):
    for i in range(1,n+1):
        k =i + 1 if(i % 2 != 0) else i
        for g in range(k,n):
            if g>=k:
                print(end="  ")
        for j in range(0,k): 
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end = " ")
n = 10
pattern(n)