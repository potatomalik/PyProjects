print('Welcome to the Password Generator.')
n_letters=int(input('How many letters you want in your password. '))
n_numbers=int(input('How many numbers you want in your password. '))
n_symbols=int(input('How many symbols you want in your password. '))

import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*']

#Easy Password:
password_easy=''
for i in range(0,n_letters):
    password_easy+=random.choice(letters)
for j in range(0,n_numbers):
    password_easy+=random.choice(numbers)
for k in range(0,n_symbols):
    password_easy+=random.choice(symbols)

print('Not Shuffled: '+password_easy)

#the hard way:
some_list=[]
for i in password_easy:
    some_list.append(i)
password_hard=''
random.shuffle(some_list)
for j in some_list:
    password_hard+=j
print('Shuffled: '+password_hard)


