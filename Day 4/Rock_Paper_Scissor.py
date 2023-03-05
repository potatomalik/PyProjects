import random
comp=['Rock','Paper','Scissor']
me=int(input('''What do you choose?
            0-Rock
            1-Paper
            2-Scissor \n'''))
ref={0:'Rock',1:'Paper',2:'Scissor'}
print('You chose '+ref[me])
me_choice=ref[me]
comp_choice=random.choice(comp)
print('The computer chose '+comp_choice)

#Checking

if me_choice==comp_choice:
    print('Draw')
elif me_choice=='Scissor':
    if comp_choice=='Rock':
        print('You Lose')
    else:
        print('You Win')
elif me_choice=='Rock':
    if comp_choice=='Paper':
        print('You Lose')
    else:
        print('You Win')
elif me_choice=='Paper':
    if comp_choice=='Scissor':
        print('You Lose')
    else:
        print('You Win')




