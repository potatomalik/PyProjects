print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
print("You're at a cross road. Where do you want to go?")
first=input('Left or Right\n')
if(first=='left' or first=='Left'):
    print("You come to a lake.There is an island in the middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    second=input('Swim or Wait?\n')
    if(second=='wait' or second=='Wait'):
        print('Yoy arrive at the island unharmed.There is a house with 3 doors. One red,one yellow and one blue')
        third=input('Which door?(Red,Blue,Yellow)\n')
        if(third=='Yellow' or third=='yellow'):
            print("You Win!")
        elif(third=='Blue' or third=='blue'):
            print("Eaten by beasts.\nGame Over.")
        elif(third=='Red' or third=="red"):
            print('Burned by fire.\nGame Over.')
        else:
            print('Game Over')
    else:
        print("Attacked by a trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")