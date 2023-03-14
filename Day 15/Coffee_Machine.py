
import os

os.system('cls')

def print_report():
    for k,v in resources.items():
        print(k,'-',v)

def sufficient_res(water,coffee,milk,coins):
    if water<=resources['Water'] and coffee<=resources['Coffee'] and milk<=resources['Milk']:
        resources['Water']-=water
        resources['Coffee']-=coffee
        resources['Milk']-=milk
        if coins>=inside_menu['cost']:
            resources['Collected Money']+=coins
        return True
    return False
 
      

def coin_counter(cost):
    final=0.25*quarter+0.10*dime+0.05*nickel+0.01*penny
    balance=final-cost
    if final<cost:
        return 0,-1
    return balance,cost
    

def coffee_decision():
    dec=sufficient_res(ingredients['water'],ingredients['coffee'],ingredients['milk'],inhand)
    if dec==True and inhand!=-1:
        if bal>0:
            print('Take your $',bal,' balance.')
            print("Here's your ",coffee,'! Have a nice day.')
        elif bal==0:
            print("Here's your ",coffee,'! Have a nice day.')
    elif dec==False:
        print('Insufficient resources...')
        print('Returning coins..')
    elif inhand==-1:
        print("Insufficient Coins...")
        print("Returning coins..")
#Main

menu={'espresso':{
        'ingredients':{ 
            'water':50,
            'coffee':18,
            'milk':0 },
        'cost':1.50
    },
    'latte':{
        'ingredients':{
            'water':200,
            'coffee':24,
            'milk':150
        },
        'cost':2.50
    },
    'capuccino':{
        'ingredients':{
            'water':250,
            'coffee':24,
            'milk':100
        },
        'cost':3.00
    }
}

resources={
    'Water':300,
    'Coffee':100,
    'Milk':200,
    'Collected Money':0
}

while(True):
    coffee=input('What would you like to have? (Espresso/Latte/Capuccino): ').lower()
    if coffee=='turn off':
        print('Machine Turned OFF!')
        break
    elif coffee=='print report':
        print_report()
        continue

    quarter=int(input('How many quarters: '))
    dime=int(input('How many dimes: '))
    nickel=int(input('How many nickels: '))
    penny=int(input('How many pennies: '))
    try:
        inside_menu=menu[coffee]
        ingredients=inside_menu['ingredients']

    except:
        print('No coffee for you!\n Check your spelling.')
        continue
    
    print(inside_menu)
    bal,inhand=coin_counter(inside_menu['cost'])
    coffee_decision()