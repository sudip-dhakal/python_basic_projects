import random

words=['america','japan','switzerland','Banglore']
word=random.choice(words)
length=len(word)

display=[]
for b in range(length):
    display+='_'
    print(display)

counter=8
game_over=False

while not game_over:
    guess=input("Enter the guess ").lower()

    for position in range(length):
        letter=word[position]
        if(letter==guess):
            display[position]=letter
        elif guess not in word:
            counter-= 1
    if counter==0:
            game_over = True
            print("You Lose")
    print(display)

    if "_" not in display:
        game_over = True
        print("Yow Win")