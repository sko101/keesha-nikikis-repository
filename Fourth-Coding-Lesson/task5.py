allScores = []
highestScore = 0
lowestScore = 100
looper = 0
while looper < 8:
    enteredScore = int(input("Please enter a score: "))
    if enteredScore <= 100 and enteredScore >= 0:
        allScores.append(enteredScore)
        looper = looper + 1
    else:
        print("That score is invalid. Please try again. It must be between 0 and 100 inclusive. ")
for counter in range(0, len(allScores)):
    if allScores[counter] > highestScore:
        highestScore = allScores[counter]
    if allScores[counter] < lowestScore:
        lowestScore = allScores[counter]
print("Highest score: " + str(highestScore))
print("Lowest score: " + str(lowestScore))
print("Range: " + str(highestScore - lowestScore))