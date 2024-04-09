# Question 16 (a)
# Examination Number:

firstName = input("What is your first name? ")
#user enters first name
surname = input("What is your surname? ")
print("Hello", firstName, surname)
print("Please select from the list of items.\n")
# \n creates a new line

print("\tItems Available") # \t creates a tab
print("------------------------")
print("1 = Book\n2 = Ruler\n3 = Pen")
print("------------------------")

shoppingItem = int(input("\nEnter the number of the item you would like: "))

if shoppingItem == 1:
    print("You bought a book")
if shoppingItem == 2:
    print("You bought a ruler")
if shoppingItem == 3:
    print("You bought a pen")
else:
    print("Invalid choice. Goodbye.")
