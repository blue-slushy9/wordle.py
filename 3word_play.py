# Different exercise -- similar to wordle
# This version of the program should apply to any and all 5-letter word and pattern combos

# The user gets to enter any five-letter word

print("Please enter a five-letter word now...")
guessword = input()
print()

# The user also gets to enter any pattern, using the characters g, b, and y;
# should also be five letters

print("Please enter your five-letter pattern now (g for green, b for blue, and y for yellow)...")
pattern = input()
print()

# Create a dictionary to store the specific letters that correspond to the pattern,
# we will use nested dictionaries to also store the positions of the letters, and/or
# how many times the letter appears in the guessword (in the case of the 'b' entries,
# since their position doesn't matter)

dict1 = {
        'b' : [],
        'g' : [],
        'y' : [] 
}

# Use a for loop to create a dictionary with g, b, or y as key values and their
# corresponding letters in the guessword as their values

for n in range(5):
    if pattern[n] == 'b': 
#        if guessword[n] not in dict['g']: 
#            if guessword[n] not in dict['y']:
        dict1['b'].append(guessword[n])
    elif pattern[n] == 'g':
        if guessword[n] not in dict1['b']:
#            if guessword[n] not in dict['y']:
                dict1['g'].append(guessword[n])
    elif pattern[n] == 'y': 
#        if guessword[n] not in dict1['g']: 
        if guessword[n] not in dict1['b']:
            dict1['y'].append(guessword[n])
    else:
        print('This is not a valid guessword-pattern combination.')
        break

print(dict1)
print()

# words that pass all of the tests will be added to the matches list as valid answers to the guessword

matches = []

# every word from the wordlist will be turned into a dictionary in order to compare with the
# guessword entered by the user, to determine if they are a match or not


wordlist = open('words.txt','r')

for word in wordlist:
    dict2 = {
        'b' : [],
        'g' : [],
        'y' : []
    }
    if not set(dict1['b']).intersection(set(word)):         
        for n in range(5):
            if pattern[n] == 'g':
                dict2['g'].append(word[n])
            elif pattern[n] == 'y':
                dict2['y'].append(word[n])
            else:
                continue
        if dict1['g'] == dict2['g']:
            for letter in dict1['y']: 
                if letter in word:
                    if dict1['y'] != dict2['y']:
                        word = word.strip()
                        matches.append(word)

print(matches)

#if dict1['g'] == dict2['g']:
#    if dict1['y'] != dict2['y']:

# Last worked on this on 3/25 -- made some progress, but I realized I will have to nest dictionaries
# within dictionaries in order to check whether the words in wordlist are a match or not.
# For instance, I would need something like this:

# {'g':{n:[2,3]}, 'b':[y], 'y': {s:[0,1]}}

# because for the y entries, they not only have to BE IN the word, but they also CANNOT be in the SAME
# position, ergo I need additional information re. their position within the original guessword, and
# for that I need nested dictionaries. I'm not sure how to create nested dictionaries at this time,
# so I will have to come back to this later and figure it out.

# 4/10 -- it occurs to me that I may be able to use tuples, as they are immutable?
