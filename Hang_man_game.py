                   		 # HANGMAN GAME...........
import random

WORDS = ["SOUTHGATE","ROMANESCO","WYOMING","LEICESTER","GARGANTULA","BOTSWANA","GONDWANALAND"]
HANGMAN = ("""
------
|     |
|
|
|
|
|
|
|
----------
""",
"""
------
|     |
|     O
|
|
|
|
|
|
----------
""",
"""
------
|     |
|     O
|    -+-
|
|
|
|
|
----------
""",
"""
------
|     |
|     O
|   /-+-
|
|
|
|
|
----------
""",
"""
------
|     |
|     O
|   /-+-/
|
|
|
|
|
----------
""",
"""
------
|     |
|     O
|   /-+-/
|     |
|
|
|
|
----------
""",
"""
------
|     |
|     O
|   /-+-/
|     |
|     |
|    |
|    |
|
----------
""",
"""
------
|     |
|     O
|   /-+-/
|     |
|     |
|    | |
|    | |
|
--------""")

word = random.choice(WORDS)
correct = word
wrong = 0   # goes till HANGMAN - 1
so_far = "-"*len(word)
used = []
while wrong < len(HANGMAN) - 1 and so_far != word:
    new = ""
    let = input("Guess the letter? ")
    let = let.upper()

    if let in word:
        print("Right!",let,"is there in the word!")
    else:
        print("HaHa! Your guy is losing time!!\n\tYou've guessed it wrong!")
        wrong+=1
    if let not in used:
        used.append(let)
    print(HANGMAN[wrong])
        
    for i in range(len(word)):
        if let==word[i]:
            new+=let
        else:
            new+=so_far[i]
    so_far = new
    print("The letters used so far are:",used)
    print("The word so far is:\t",so_far)
    print("\n\t===================================================================\n")
if so_far == word:
    print("Congrats! You have guessed the word right!!")
if wrong == len(HANGMAN)-1:
    print("Alas! Your man has been hanged!")
print("And, the word was:\t",word)
input("Pres Enter to Exit")
