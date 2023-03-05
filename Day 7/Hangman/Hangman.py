import random
import hangman_words
word=random.choice(hangman_words.words_list)
#print(f'The random word is {word}')
guesses=[]
blanks=[]
for i in range(0,len(word)):
    blanks.append('_')
life=6
while True:
    choice=input("Guess a word.\t").lower()
    if choice in guesses:
        print('Already Guessed!')
        continue
    else:
        guesses.append(choice)
        for pos in range(len(word)):
            if word[pos]==choice:
                print(f"{choice} is in the word.")
                blanks[pos]=choice
        if choice not in word:
            life-=1
            print(f"The letter {choice} is not in the word.")
            print('LOST LIFE',life)
            if life==0:
                print('GAME OVER!!')
                print('The correct word is: '+word)
                exit(0)
                
        
    print(blanks)
    if "_" not in blanks:
        print('Congratulatons.')
        print(f"You guessed {word} correctly.")
        print('You Win!!')
        break