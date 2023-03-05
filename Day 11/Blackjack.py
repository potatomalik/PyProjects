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
                if sum_of_list(user)>21:
                    #print('Sum greater then 21, You Lose!')
                    break
                want_comp=want_card(computer)
                for _ in range(1):
                    if want_comp+sum_of_list(computer)>21:
                        break
                    else:
                        computer.append(want_comp)
                        
            elif want=='n':
                break
            else:
                print('INVALID INPUT')
        
        print(f"Your cards: {user}, Score: {sum_of_list(user)}\nComputer's cards: {computer}, Score: {sum_of_list(computer)}")
        if sum_of_list(user)>21:
            print('Sum greater than 21, You Lose!')
        elif sum_of_list(user)>sum_of_list(computer):
            print('You Win!')
        elif sum_of_list(user)<sum_of_list(computer):
            print('You Lose!')
        elif sum_of_list(user)==sum_of_list(computer):
            print('Game Drawn!')
        
    elif prompt=='n':
        break
    else:
        print('INVALID INPUT')


