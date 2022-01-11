i=0
while i<=5:
    secret_guess_num=5
    guess=int(input("enter your gues number="))
    if secret_guess_num==guess:
        print("congrats! your guess is correct")
        break
    elif secret_guess_num<guess:
        print("your guess is greater then secret num",guess)
    elif secret_guess_num>guess:
        print("your guess  is  less then  secret num",guess)
    else:
        print("guessing is rong")
    i=i+1

