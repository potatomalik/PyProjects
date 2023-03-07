from game_data import data
import random
import os

def game():
    A=random.choice(data)
    #name_a,description_a,country_a=A['name'],A['description'],A['country']
    #print(f'Compare A:{name_a}, a {description_a}, from {country_a}')
    #print('V/s')
    score=0
    while True:
        name_a,description_a,country_a=A['name'],A['description'],A['country']
        print(f'Compare A:{name_a}, a {description_a}, from {country_a}')
        print('V/s')
        B=random.choice(data)
        name_b,description_b,country_b=B['name'],B['description'],B['country']
        print(f'Against B:{name_b}, a {description_b}, from {country_b}')
        pop_a,pop_b=A['follower_count'],B['follower_count']

        
        guess=input("Who has more followers? Type 'A' or 'B'.").lower()
        if guess=='a' and pop_a>pop_b:
            os.system('cls')
            score+=1
            print(f"You're right! Current score={score}")
        elif guess=='b' and pop_b>pop_a:
            os.system('cls')
            score+=1
            print(f"You're right! Current score={score}")
            A=B
        else:
            os.system('cls')
            print(f"You're Wrong, Score: {score}")
            break

game()


    

