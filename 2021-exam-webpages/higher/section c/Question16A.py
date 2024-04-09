# Question 16(a)
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False

#ask user for input and assign to variable
#change the words to lower-case
word1 = input("Enter the first word: ")
w1 = word1.lower()
word2 = input("Enter the second word: ")
w2 = word2.lower()

# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(w1) == sorted(w2)):
    print(word1, "is an anagram of", word2)
else:
    print(word1, "is NOT an anagram of", word2)

# Checks if the words are 
# anagrams of each other again.
result = is_anagram(w1, w2)
if result == True:
    print(word1, "is an anagram of", word2)
else:
    print(word1, "is NOT an anagram of", word2)

# Ask for the user to enter a phrase
phrase = input("Enter a phrase: ")
#count number of spaces
num_spaces = phrase.count(" ")
#change to lower-case letters
ph_l = phrase.lower() 
ph_s = sorted(ph_l)

#function removes spaces from phrase
def phrase_spaces(ph_s):
    counter = 0
    while counter<num_spaces:
        ph_s.remove(" ")
        counter+=1
    return ph_s

ph = phrase_spaces(ph_s)

def is_anagram_phrase(w1, w2, ph):
    if ph==sorted(w1):
        print( word1, "is an anagram of", phrase)
    else:
        print(word1, "is NOT an anagram of", phrase)
    if ph==sorted(w2):
        print(word2, "is an anagram of", phrase)
    else:
        print(word2, "is NOT an anagram of", phrase)

is_anagram_phrase(w1, w2, ph)






