names = ["Amir", "Beth", "Callum", "Dion", "Emma"]
scores = [67, 81, 54, 72, 93]

highestScore = scores[0]
indexOfHighest = 0
lowestScore = scores[0]
indexOfLowest = 0

for counter in range(1, len(scores)):
    if scores[counter] > highestScore:
        highestScore = scores[counter]
        indexOfHighest = counter
    if scores[counter] < lowestScore:
        lowestScore = scores[counter]
        indexOfLowest = counter

print("Highest: " + str(names[indexOfHighest]) + " with " + str(highestScore))
print("Lowest: " + str(names[indexOfLowest]) + "with " + str(lowestScore))