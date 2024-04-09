# Question 16(a)
# Examination Number:

pin = "1579"
loggedIn = False
failedAttempts = 0


while loggedIn==False:
    # ask user for input and assign to variable
    userTry = input("Enter PIN: ")
    if userTry == pin:
        print("Welcome")
        loggedIn = True
    else:
        print("Incorrect PIN")
        failedAttempts += 1
        if failedAttempts == 3:
            print("You have entered the PIN incorrectly 3 times")
