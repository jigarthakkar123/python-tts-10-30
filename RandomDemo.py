import random

#print(random.randint(100000,999999))
#print(random.choice([1,90,77,444,555,"tops","python",True,False]))

num=random.randint(1,20)

while True:
    guess=int(input("Guess A Number Between 1 To 20 : "))

    
    if guess==num:
        print("You Guessed A Correct Number")
        break
    elif guess>num:
        print("You Guessed Greater Number")
    elif guess<num:
        print("You Guessed A Smaller Number")
        
