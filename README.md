🎯 Find the O

A simple command-line guessing game built in Python. Three positions are shuffled — one holds the letter O, the other two are empty. Guess the right index (0, 1, or 2) and win!

📋 How It Works


A list [" ", "O", " "] is shuffled randomly using random.shuffle().
The player is asked to guess a position — 0, 1, or 2.
The game checks if the guessed position holds "O" and prints whether the guess was correct or incorrect.
The final shuffled list is displayed so you can see where O actually was.
