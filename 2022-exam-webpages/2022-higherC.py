# Question 16(a)
# Examination Number:
from random import randint

print("Dice simulation and analysis program")
results = []
dice = [1, 2, 3, 4, 5, 6]
frequencies = [0, 0, 0, 0, 0, 0]

# Loop 100 times
for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results

    # Start to build up a list of frequencies for each value thrown
    if throw_result == 1:
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
        frequencies[1] = frequencies[1] + 1
    elif throw_result == 3:
        frequencies[2] = frequencies[2] + 1
    elif throw_result == 4:
        frequencies[3] = frequencies[3] + 1
    elif throw_result == 5:
        frequencies[4] = frequencies[4] + 1
    elif throw_result == 6:
        frequencies[5] = frequencies[5] + 1
    

print()
print("Results: ", results)
print("Frequencies: ", frequencies)

print("Dice", "\t", "Frequencies")
print("----", "\t", "-----------")
for y in range(6):
    print(dice[y], "\t", frequencies[y])

#find the maximum value in frequencies
max = max(frequencies)
#find the index number of the max value
indexNumber = frequencies.index(max)

print(indexNumber+1, " was rolled the most often (", max, " times)", sep="")

for g in frequencies:
    print(g*"*")