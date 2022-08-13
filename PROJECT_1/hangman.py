#KIRBIES IN ACTION
from englishWord import word
import random
import string
from hangmanVisual import lives_visual_dict
def guess_word_valid():
    wordChoice = random.choice(word)
    if(" " in wordChoice or "-" in wordChoice):
        guess_word_valid()
    return wordChoice

def hangman():
    guess_word = guess_word_valid().upper()
    print(guess_word)
    lives = 7
    letters = set(guess_word)
    used_letter = set()
    alphabet = set(string.ascii_uppercase)
    
    while len(letters)>0 and lives>0:
        word_list = [display if display in used_letter else '_' for display in guess_word]
        print(word_list)
        print("Used letter : "+ ' '.join(used_letter))
        print(lives_visual_dict[lives])
        print("Remaining lives : " , lives)
        user_letter = input("Your letter : ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)
                print("Nice")
            else:
                print("Wrong")
                lives-=1
        else:
            print("use different letter")
        
    print(lives_visual_dict[lives])
    if lives>0:
        print("You won, great!",guess_word)
    else:
        print("DAMN LOSER", guess_word)
hangman()


