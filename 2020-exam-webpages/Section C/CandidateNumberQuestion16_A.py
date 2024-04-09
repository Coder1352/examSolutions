# Question 16(a)
# Examination Number:

# Prompt the user to enter a password and store the ...
# value entered in the variable password
password = input("Enter a password: ")

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

# A variable to store all the uppercase letters in the alphabet
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# A variable to store all digits
DIGITS = "0123456789"

# The variables lowercase, uppercase and digit indicate the presence or ...
# absence of lowercase and uppercase characters and digits in the password
lowercase = False # True if password contains a lowercase letter
uppercase = False # True if password contains an uppercase letter
digit = False # True if password contains a digit
firstDigit = False # True if first character is a digit
lastDigit = False # True if last character is a digit
firstLastDigit = False # True if first and last characters are digits
allDigits = False # True if all characters are digits

# Loop through each character in the password and ...
# check the password for specific characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in UPPER_CASE_LETTERS:
        uppercase = True
    if character in DIGITS:
        digit = True

#check if first/last characters are digits

if password[0] in DIGITS:
    firstDigit = True
    
if password[-1] in DIGITS:
    lastDigit = True
    
#check if all characters are digits
    
if password.isdigit():
    allDigits = True
        
# Calculate the score based on the rules

#initialise score
score = 0

# Rule 1
if len(password) > 7:
    score = score + 5

if len(password) >3 and len(password) <7:
    score = score + 2
    
if len(password) <4:
    score = score -2

# Rule 2
if lowercase:
    score = score + 1

# Rule 3
if lowercase and uppercase:
    score = score + 5
    
#Rule 4
if uppercase:
    score = score + 2
    
#Rule 5
if digit:
    score = score + 5
    
#Rule 6
if firstDigit:
    score = score + 1
    
if lastDigit:
    score = score + 1
    
if firstDigit and lastDigit:
    score = score + 2
    
#Rule 7
if allDigits:
    score = score - 10
    
#Display the password
print("Password:", password)

# Display the score
print("Score:", score)