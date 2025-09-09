# A_word_guessing_game or

# 🎮 Hangman Game (Python CLI)

A **classic Hangman game** implemented in Python where the player must guess a randomly chosen word before the stick figure is fully drawn.  
This project demonstrates the use of **loops, conditionals, functions, and user interaction** via the terminal.

---

## 🚀 Features
- Randomly selects a word from a **predefined word bank**.  
- Displays the **hangman figure stage** as you make incorrect guesses.  
- Tracks **guessed letters** to prevent duplicates.  
- Win or lose messages based on game outcome.  
- Simple, beginner-friendly, and completely **text-based**.

---

## 🛠️ Technologies Used
- **Python 3.x**
- No external libraries required (only the `random` module).

-

---

## 🎯 How to Play
1. **Clone this repository:**
   ```bash
   git clone https://github.com/kishu01karb/A_word_guessing_game.git
   cd A_word_guessing_game

python A_word_guessing_game.py

Instructions:

You will see a series of underscores representing a hidden word.

Type a single letter and press Enter to guess.

If the letter is correct, it will appear in its position.

If incorrect, a part of the hangman will be drawn.

Goal: Guess the entire word before the hangman figure is complete.
Welcome to Hangman!
Try to guess the word before the hangman is complete!

       ______
       |    |
       |
       |
       |
       |
    ___|___

Current Word: _ _ _ _ _
Guessed letters:
Wrong Guesses: 0/6

Guess a Letter for Word: a
Great guess!

Current Word: a _ _ _ _
Guessed letters: a
Wrong Guesses: 0/6

apple, ball, tree, frog, moon, road, king, wolf, goat, snow, star etc
You can customize it by editing the word_bank list inside the code:


