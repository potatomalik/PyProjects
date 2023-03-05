import os
def clear():
    os.system('cls')

bid_list={}

while True:
    name_bidder=input('Enter your name: ')
    bid=int(input('Enter your bid: $'))
    bid_list[name_bidder]=bid
    next=input('Are there any other bidders?: (Y/N) ').lower()
    if next=='y':
        clear()
    else:
        break
#print(bid_list)
maxval=max(bid_list)
#print(maxval)
print(f'The bid goes to {maxval} for ${bid_list[maxval]}')