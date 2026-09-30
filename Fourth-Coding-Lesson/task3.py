numbers = [23, 8, 41, 16, 5, 37, 12]
highestNumber = -10000000000000000000000000000
lowestNumber = 10000000000000000000000000000
for counter in range(len(numbers)):
    if numbers[counter] > highestNumber:
        highestNumber = numbers[counter]
    if numbers[counter] < lowestNumber:
        lowestNumber = numbers[counter]
print("Highest value: " + str(highestNumber))
print("Lowest value: " + str(lowestNumber))