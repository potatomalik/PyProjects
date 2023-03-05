#ENCODE FOR REFERENCE
def encode(text,shift):
    encoded_msg=''
    for letter in text:
        position=alphabets.index(letter)
        new_position=position+shift
        if new_position>len(alphabets):
            new_position=new_position-len(alphabets)
        encoded_msg+=alphabets[new_position]
    print(f'The encrypted message - {encoded_msg}.')

#DECODE FOR REFERENCE
def decode(text,shift):
    decoded_msg=''
    for letter in text:
        position=alphabets.index(letter)
        new_pos=position-shift
        if new_pos<0:
            new_pos=len(alphabets)+new_pos
        decoded_msg+=alphabets[new_pos]
    print(f'The decrypted message - {decoded_msg}.')

#Merged the encode and decode function into a single function.
def caesar(text,shift,direction):
    new_msg=''
    if direction=='decode':
            shift=-shift
    for letter in text:
        if letter not in alphabets:
            new_msg+=letter
            continue
        position = alphabets.index(letter)
        new_pos=position + shift
        if new_pos>=len(alphabets):
            new_pos=new_pos-len(alphabets)
        if new_pos<0:
            new_pos=len(alphabets)+new_pos
        new_msg+=alphabets[new_pos]
    print(f'The {direction}d message - {new_msg}')

#MAIN
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
    direction=input("Type 'encode' to encypt a message and Type 'decode' to decrypt a message: ").lower()
    text=input('Enter the text: ').lower()
    shift=int(input('Enter the shift number: '))
    shift=shift % 26
    caesar(text,shift,direction)
    
    choice=input('Do you want to continue? (Yes/No) ').lower()
    if choice=='no':
        exit(0)
    else:
        continue
