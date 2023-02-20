import random

random_number=random.randint(1,100)
while(True):
    user_input=int(input("Choose the number between 1 and 100 "))
    if(random_number==user_input):
        print("You guessed correctly ")
        break
    elif(random_number>user_input):
        print("You guessed the number lesser than actually it is ")
    else:
        print("You guessed the number greater than actually it is ")
