# # Create a list of all the words that start with the letter "p" and print out the whole list
#
# f = open('words.txt','r')
#
# p_word_list = []
#
# for p_word in f:
#     if p_word[0] == 'p':
#         p_word = p_word.strip()
#         p_word_list.append(p_word)
#
# print(p_word_list)
# print()
#
# # Create a list of all the words that contain the letter "q" and print out the whole list
#
# f = open('words.txt','r')
#
# q_word_list = []
#
# for q_word in f:
#     if 'q' in q_word:
#         q_word = q_word.strip()
#         q_word_list.append(q_word)
#
# print(q_word_list)
# print()
#
# # Create a list of all the words that do not contain the letter "s"
#
# f = open('words.txt','r')
#
# no_s_list = []
#
# for no_s_word in f:
#     if 's' not in no_s_word:
#         no_s_word = no_s_word.strip()
#         no_s_list.append(no_s_word)
#
# print(no_s_list)
# print()
#
# # Create a list of all the words that have the letter "e", but it can't be in the 2nd position.
#
# f = open('words.txt','r')
#
# e_word_list = []
#
# for e_word in f:
#     if 'e' in e_word and e_word[1] != 'e':
#         e_word = e_word.strip()
#         e_word_list.append(e_word)
#
# print(e_word_list)
# print()
#

# # Different exercise -- similar to wordle
#
# guess = "raise"
#
# # g means same letter in same position
#
# # b means letter not in word at all
#
# # y means letter is in word but NOT in that position
#
# pattern = "gbbby"
#
# f = open('words.txt','r')
#
# possibles = []
#
# for possible in f:
#     if possible[0] == guess[0] and guess[1-3] not in possible and guess[4] in possible:
#         possible = possible.strip()
#         possibles.append(possible)
#
# print(possibles)

# Different exercise -- similar to wordle
# This version of the program should apply to any and all word and pattern combos

dict = {
    "g":[],
    "b":[],
    "y":[]
}

# The user gets to enter any word

print("Please enter your word now...")
guessword = input()
print(guessword)
print()

# The user also gets to enter any pattern, using the characters g, b, and y;
# should be exactly the same length as the word they entered

print("Please enter your pattern now...")
pattern = input()
print(pattern)
print()

# Use a for loop to create a dictionary with g, b, or y as key values and their
# corresponding letters in the guess-word as their values

n = 0

for n in range(len(guessword)):
    if pattern[n] == "g" and guessword[n] not in dict["b"] and guessword[n] not in dict["y"]:
        dict["g"].append(f"{guessword[n]}{n}")
    elif pattern[n] == "b" and guessword[n] not in dict["g"] and guessword[n] not in dict["y"]:
        dict["b"].append(f"{guessword[n]}")
    elif pattern[n] == "y" and guessword[n] not in dict["g"] and guessword[n] not in dict["b"]:
        dict["y"].append(f"{guessword[n]}{n}")
    else:
        print("This is not a valid guessword-pattern combination.")
        break
    n = n + 1

print(dict)
print()

# words that pass all of the tests will be added to the matches list as valid answers to the guessword

matches = []

# every word from the wordlist will be turned into a dictionary in order to compare with the
# guessword entered by the user, to determine if they are a match or not

dict2 = {
    "g":[],
    "b":[],
    "y":[]
}

wordlist = open('words.txt','r')

for word in wordlist:
    if len(guessword) == len(word):
        if dict["b"] not in word:
            for n in range(len(word)):
                if pattern[n] == "g" and word[n] not in dict["y"]:
                    dict2["g"].append(f"{word[n]}{n}")
                elif pattern[n] == "y" and word[n] not in dict["g"]:
                    dict2["y"].append(f"{word[n]}{n}")
            n = n + 1

    if dict["g"] == dict2["g"] and dict["y"] != dict2["y"]:

# Last worked on this on 3/25 -- made some progress, but I realized I will have to nest dictionaries
# within dictionaries in order to check whether the words in wordlist are a match or not.
# For instance, I would need something like this:

# {'g':{n:[2,3]}, 'b':[y], 'y': {s:[0,1]}}

# because for the y entries, they not only have to BE IN the word, but they also CANNOT be in the SAME
# position, ergo I need additional information re. their position within the original guessword, and
# for that I need nested dictionaries. I'm not sure how to create nested dictionaries at this time,
# so I will have to come back to this later and figure it out.
