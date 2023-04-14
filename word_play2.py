# New exercise, similar to wordle

# g means same letter in same position

# b means letter not in word at all

# y means letter is in word but NOT in that position

# pattern = "gbbby"

guess = "raise"

f = open('words.txt','r')

possibles = []

for possible in f:
    if guess[0] == possible[0]: 
        if not set(guess[1:4]).intersection(set(possible)):        
            if guess[4] in possible: 
                if guess[4] != possible[4]:
                    if guess.count('e') == possible.count('e'):
                        possible = possible.strip()
                        possibles.append(possible)

print(possibles)
