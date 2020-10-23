import random, time



def play_again():
    answer = input('Would you like to play again? yes/no: ').lower()
    if answer == 'y' or answer == 'yes':
        play_game()

    elif answer == 'n' or answer == 'no':
        print("Thanks for Playing!")
        time.sleep(2)
        exit()
    else:
        pass

def get_word():
    words = ['pear', 'apple', 'banana', 'grape', 'pineapple', 'orange', 'apricot', 'grapefruit', 'eggplant', 'cabbage', 'broccoli', 'lavender', 'spinach', 'cauliflower', 'lettuce', 'onions', 'pepper', 'carrot', 'tomato', 'strawberry', 'mango', 'pumpkin', 'celery', 'cucumber', 'garlic', 'avocado', 'kiwi', 'blueberry', 'raspberry', 'mandarin']
    return random.choice(words)



name = input("Please enter your name: ")
print("Hello", name, "let's Begin!")
time.sleep(1)
print("Try to guess the word chosen by the computer!")
time.sleep(1)

print("You can only guess 1 letter at a time")
print("Press Enter after typing a letter")
time.sleep(2)
print("Let's Start!!")
time.sleep(1)

def play_game  ():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries = 10
    guessed = False

    print('The word contains ', len(word), ' letters.')
    print(len(word) * '*')

    while guessed == False and tries > 0:
        print("You have " + str(tries) + ' tries left')
        guess = input("Please enter one letter. ").lower()

        if len(guess) == 1:
            if guess not in alphabet:
                print("You have not entered a letter!")
            elif guess in letters_guessed:
                print("You already guessed this letter, try another!")
            elif guess not in word:
                print("That letter is not part of the word!")
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print("Good Job, You guessed a letter!")
                letters_guessed.append(guess)

            else:
                print("How did you even get this message? Go away!")

            if len(guess) != 1:
                print("Please only put in 1 letter!") 

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == word:
            print("Great Job ", name, " You guessed the word")
            guessed == True
            play_again()
        elif tries == 0:
            print("You are out of tries, better luck next time!")
            print("The word was: ", word)
          
    
    play_again()


play_game()