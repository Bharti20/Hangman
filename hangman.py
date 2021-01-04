import string
from words import choose_word
from images import IMAGES

# # End of helper code
# # -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    if secret_word ==get_guessed_word(secret_word, letters_guessed):
        return True
    
    return False
def get_hint(secret_word, letters_guessed):
    import random
    letters_not_guessed = []

    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)

        index += 1

    return random.choice(letters_not_guessed) 
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word= guessed_word+secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    return letters_left 
        
def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    letters_guessed = []
    total_lives = remaining_lives = 8
    images_selection = [0, 1, 2, 3, 4, 5, 6, 7]
    user_difficulty_choice = input("Aap kis level pe khelna chahte hai ""\n""a for eassy""\n""b for medium""\n""c for hard--")
    if user_difficulty_choice == "b":
        total_lives = remaining_lives = 6
        images_selection = [1, 2, 3, 4, 6, 7]

    elif user_difficulty_choice == "c":
        total_lives = remaining_lives = 4
        images_selection = [1, 3, 5, 7]
    else:
        if user_difficulty_choice!="a":
            print("your choice is valid""\n""game is started in easy level" )
    letters_guessed = [] 
    while remaining_lives>0:
    
      available_letters = get_available_letters(letters_guessed)
      print ("Available letters: " + available_letters)

      guess = input("Please guess a letter: ")
      if guess == "hint":
        letter = get_hint(secret_word, letters_guessed)
      else:
          letter = guess.lower()
          if letter not in available_letters:
              print("invalid input")
              continue
      if letter in secret_word:
          letters_guessed.append(letter)
          print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          print("")
      
    
          if is_word_guessed(secret_word, letters_guessed) == True:
            print (" * * Congratulations, you won! * * ")
            print ("")
            break
      else:
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print(IMAGES[images_selection[total_lives-remaining_lives]])
            remaining_lives -= 1 
            print("Remaining Lives : "+str(remaining_lives))
            print("")
            
            
    else:
        print("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")

secret_word = choose_word()
hangman(secret_word)