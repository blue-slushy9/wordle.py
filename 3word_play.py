# Different exercise -- similar to wordle
# This version of the program should apply to any and all 5-letter word and pattern combos

# The user gets to enter any five-letter word

print("This program is similar to Wordle! Please enter a five-letter word now...")
guessword = input()
print()

# The user also gets to enter any pattern, using the characters g, b, and y;
# should also be five letters

print("Please enter your five-letter pattern now (g for green, b for blue, and y for yellow)...")
pattern = input()
print()

# we will create a dictionary to store the combinations of the colors and letters
# we will use lists within the dictionary to store all of the letters corresponding
# to the color

dict1 = {
        'b' : [],
        'g' : [],
        'y' : [] 
}

# Use a for loop to create a dictionary with g, b, or y as key values and their
# corresponding letters in the guessword as their values

for n in range(5):
    if pattern[n] == 'b': 
        dict1['b'].append(guessword[n])
    elif pattern[n] == 'g':
        if guessword[n] not in dict1['b']:
            dict1['g'].append(guessword[n])
    elif pattern[n] == 'y': 
        if guessword[n] not in dict1['b']:
            dict1['y'].append(guessword[n])
    else:
        print('This is not a valid color-guessword combination.')
        break

print(dict1)
print()

# words that pass all of the below tests will be added to the matches list as valid answers to the guessword

matches = []

# every word from the wordlist will be turned into a dictionary in order to compare with the
# guessword entered by the user, to determine if they are a match or not

wordlist = open('words.txt','r')

for word in wordlist:
    dict2 = {
#        'b' : [],
        'g' : [],
        'y' : []
    }
    if not set(dict1['b']).intersection(set(word)):         
        for n in range(5):
            if pattern[n] == 'b':
                continue
            elif pattern[n] == 'g':
                dict2['g'].append(word[n])
            elif pattern[n] == 'y':
                dict2['y'].append(word[n])
        if dict1['g'] == dict2['g']:
            for letter in dict1['y']: 
                if letter in word:
                    if dict1['y'] != dict2['y']:
                        word = word.strip()
                        matches.append(word)

print(matches)
