import tkinter as tk
import random

def play_hangman():

    
    word_list = ["python", "programming", "language", "computer", "science"]
    word = random.choice(word_list)
    word = word.upper()
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()
    word_guessed = set()
    tries = 6

    
    print("Let's play hangman!")
    while (len(word_letters) > 0) and (tries > 0):
        print("You have", tries, "tries left.")
        print("Used letters:", " ".join(used_letters))
        print("Word: ", " ".join(letter if letter in word_guessed else "_" for letter in word))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_guessed.add(user_letter)
                word_letters.discard(user_letter)
            else:
                tries -= 1
        else:
            print("You have already used that letter. Try again.")
    if tries > 0:
        print("Congratulations! The word was", word + ".")
    else:
        print("Sorry, you ran out of tries. The word was", word + ". Better luck next time!")

root = tk.Tk()
root.title("Hangman Game")

label = tk.Label(root, text="Welcome to the Hangman Game!")
label.pack()

play_button = tk.Button(root, text="Play", command=play_hangman)
play_button.pack()

root.mainloop()

