i=0
while i<=50:
    i=i+1
    if i%3==0 and i%5==0:
        print("fizzbuzz")
        continue
    if i%3==0:
        print("fizz")
        continue
    if i%5==0:
        print("buzz")
        continue
    print(i)