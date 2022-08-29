country_code=input("enter a country code ")
product_code=input("enter a product code ")
weight_in_kg=float(input("enter weight "))
if country_code=="uk" and weight_in_kg<5:
    if "123" in product_code :
        print(5*1.2*(1+0.18)) 
elif country_code=="uk" and weight_in_kg>=5:
   if "234" in product_code:
        print(5*1.5*(1+0.18)) 
elif country_code=="us" and weight_in_kg<10 :
    if "123" in product_code :
        print(5*1.2*(1+0.18)) 
elif country_code=="us" and weight_in_kg>=10:
    if "234" in product_code:
        print(5*1.5*(1+0.18)) 
    else : 
        print("5","inr")   
i=1
sum=1
while i<10:
    i+=1
    sum=sum**i
    
    print(i,sum)
