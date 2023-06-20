# This version of the program should apply to any and all 5-letter word and 
# pattern combos;

############################

# The sys.exit() method is used to terminate execution of the code, I will use
# it in case the user enters invalid input, e.g. a four-letter guessword or
# pattern;
from sys import exit

# Throughout this program, I use many print() statements to increase
# legibility in the terminal, e.g. below;
print()

print("This program is similar to Wordle! Please enter a five-letter word now...")
print()
guessword = input()
print()

# Use the strip() method to eliminate any whitespace before and/or after the 
# guessword;
guessword = guessword.strip()

# This version of the game only accepts five-letter guesswords, ergo if the 
# player enters a word of any length other than five, we exit the program;
if len(guessword) != 5:
    print("Sorry, you have entered a guessword that is not equal to five\n"
            "characters in length. The game will now end, please start over\n"
            "from the beginning if you'd like to play again :)")
    print()
    exit()

# The user also gets to enter any pattern, using the characters b, g, and y;
# this pattern should also be five letters;
print("Please enter your five-letter pattern now: b for blue, g for green,\n" 
        "and y for yellow. Blue means the letter is NOT in the word at all,\n"
        "green means the letter IS in the word in that SAME position,\n"
        "and yellow means the letter IS in the word but NOT in that position.")
print()
pattern = input()
print()

# Use the strip() method to eliminate any whitespace before and/or after the 
# pattern;
pattern = pattern.strip()

# This version of the game only accepts five-letter patterns, ergo if the 
# player enters a pattern of any length other than five, we exit the program;
if len(pattern) != 5:
    print("Sorry, you have entered a pattern that is not equal to five\n"
            "characters in length. The game will now end, please start over\n"
            "from the beginning if you'd like to play again :)")
    print()
    exit()

# We will create a dictionary to store the combinations of the colors and letters;
# we will use lists within the dictionary to store all of the letters corresponding
# to the color;
dict1 = {
        'b' : [],
        'g' : [],
        'y' : [] 
}

# Use a for loop to create a dictionary with b, g, or y as keys; and then their
# corresponding letters in the guessword as their values;
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

#print(dict1)
#print()

# Words that pass all of the below tests will be added to the matches list as 
# valid answers to the guessword;
matches = []

# Every word from the wordlist will be turned into a dictionary in order to 
# compare with the guessword entered by the user, to determine if they are a 
# match or not;
wordlist = open('words.txt','r')

# Loop through every word in the wordlist to look for potential matches;
for matchword in wordlist:
    
    # dict2 only exists for one iteration of the loop at a time, only for the
    # purpose of comparing the given matchword with the guessword entered by user;
    # strictly speaking, we are actually comparing the DICTIONARIES derived
    # from the words, as opposed to the words themselves;
    dict2 = {
#       'b' : [], # We don't need a 'b' key because it signifies the letter is
        'g' : [], # not in the word at all, I only left it in as a visual aid;
        'y' : []
    }
    
    # set() function creates a set object, i.e. an unordered collection of
    # UNIQUE elements; it takes an iterable as an argument; intersection()
    # method is used to check for intersecting elements between two or more
    # sets; the 'not' ensures the following code only runs if there are NO
    # common elements between dict1['b'] (blue letters) and word, because blue
    # letters are NOT in the word AT ALL;
    if not set(dict1['b']).intersection(set(matchword)):         
        
        # All the words in this game are five letters long, so we set range
        # to 5 (exclusive);
        for n in range(5):
            
            # Any time we hit a 'b' in our pattern, we use continue to skip 
            # ahead to the next iteration of our for loop, since the 'b'
            # letters are not in our guessword at all, so it doesn't matter
            # what letter is in that position in the potential matchword;
            if pattern[n] == 'b':
                continue
            
            # 'g' and 'y' letters get added to dict2 along with their
            # positions in the potential matchword, for comparison with dict1;
            elif pattern[n] == 'g':
                dict2['g'].append(matchword[n])
            
            elif pattern[n] == 'y':
                dict2['y'].append(matchword[n])
        
        # The 'g' values just be an exact match;
        if dict1['g'] == dict2['g']:
            
            # Loop through the 'y' letters in dict1...
            for letter in dict1['y']: 
                
                # Check whether the 'y' letter is in the potential matchword
                # at all...
                if letter in matchword:
                    
                    # then if it is, check whether the positions of the 'y'
                    # letters are NOT the same (yellow means position should
                    # NOT be the same, but letter should be in matchword);
                    if dict1['y'] != dict2['y']:
                        
                        # If the potential matchword passes these tests, first
                        # use strip() to remove any leading or trailing white-
                        # spaces...
                        matchword = matchword.strip()
                        
                        # finally, add the matchword to matches list;
                        matches.append(matchword)

# If there are zero or fewer entries in the matches list...
if len(matches) <= 0:
    print("Sorry, there were no matches based on your guessword and pattern.")

else:
    # Use join() method to convert matches list to string, with the matchwords
    # separated by a comma and a space;
    matches = (', '.join(matches))
    
    print(f"These are your potential matches: {matches}")
print()
