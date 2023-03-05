import random

def add_cards(cards_main,some_main):
    for i in range(2):
        num=random.choice(cards_main)
        some_main.append(num)
    
def want_card(some_deck):
    num=random.choice(cards)
    if num==11 and (sum_of_list(some_deck)+11)>21:
        num=1
    #some_deck.append(num)
    return num


def sum_of_list(lists):
    sum=0
    for i in lists:
        sum+=i
    return sum

def blackjack(deck):
    if sum_of_list(deck)==21 and len(deck)==2:
        return 0 
    
def compare():
    if sum_of_list(user)==sum_of_list(computer):
            print('Game Drawn!')
    elif blackjack(user)==0:
            print('You Win with a Blackjack!')
    elif blackjack(computer)==0:
            print('You Lose, Opponent has Blackjack!')
    elif sum_of_list(user)>21:
            print('You went over, You Lose!')
    elif sum_of_list(computer)>21:
            print('Computer went over, You Won!')
    elif sum_of_list(user)>sum_of_list(computer):
            print('You Win!')
    elif sum_of_list(user)<sum_of_list(computer):
            print('You Lose!')
    elif sum_of_list(user)==sum_of_list(computer):
            print('Game Drawn!')
    
#MAIN 

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]


while True:
    prompt=input('Do you want to play a game of blackjack? (Y/N) ').lower()
    user=[]
    computer=[]
    
    if prompt=='y':
        add_cards(cards,user)
        add_cards(cards,computer)
        print(f'Your cards:{user} ,Current score: {sum_of_list(user)}')
        print(f"Computer's first card: {computer[0]}")
        
        while True:
            want=input('Do you want to get another card? (Y/N)').lower()
            if want=='y':
                want_user=want_card(user)
                user.append(want_user)
                print(f'Now your cards: {user} ,Current score: {sum_of_list(user)}')
                if sum_of_list(user)>21 or blackjack(user)==0 or blackjack(computer)==0:
                    #print('Sum greater then 21, You Lose!')
                    break
                want_comp=want_card(computer)
                for _ in range(1):
                    if sum_of_list(computer)>17:
                        break
                    else:
                        computer.append(want_comp)
                        
            elif want=='n':
                break
            else:
                print('INVALID INPUT')
        
        print(f"Your cards: {user}, Score: {sum_of_list(user)}\nComputer's cards: {computer}, Score: {sum_of_list(computer)}")
        compare()
        
    elif prompt=='n':
        break
    else:
        print('INVALID INPUT')


