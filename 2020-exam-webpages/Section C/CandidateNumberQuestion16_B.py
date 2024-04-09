# Question 16(b)
# Examination Number:

# A variable to store all the lower case letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

def calculate_score(password):

    # The variables lowercase and uppercase indicate the presence or
    # absence of lowercase and uppercase characters in the password
    lowercase = False #True if password contains a lowercase letter
    uppercase = False #True if password contains an uppercase letter

    # Loop through each character in the password and ...
    # ... check the password for specific characters
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True

    # Calculate the score based on the rules

    score = 0

    # Rule 1
    if len(password) > 7:
        score = score + 5

    # Rule 2
    if lowercase:
        score = score + 1

    # Rule 3
    if lowercase and uppercase:
        score = score + 5

    return score

# Test driver
test_passwords = ["sun", "Sun", "Sunshine", "12345", "123456789"]

#Replace element in list
test_passwords[4] = "Moonlight"
 
#Create new list
pass_score_list = []

print("Score\t Password\n-----\t --------")

#Loop through list and run function to get score
#Add scores to list
for password in test_passwords:
    pass_score = calculate_score(password)
    pass_score_list.append(pass_score)
    print(pass_score, "\t",password)

#Calculate lowest score in the list, get the index of that value, and print the statement
lowest_score = min(pass_score_list)
x = pass_score_list.index(lowest_score)
print("\nThe weakest password is:", test_passwords[x])
print("Score:", lowest_score)

#Calculate if the password is strong
def is_strong(password):
    
    strong = False # True if password is strong
    
    score = calculate_score(password)
    if score > 9:
        strong = True
        
    return strong

print("\nThe strong passwords are:")

# Loop through list and print password if it's strong
for password in test_passwords:
    strong_password = is_strong(password)
    if strong_password == True:
        print(password)
