# Validity checks!

# Variables:
integersCheck = False
from0to255Check = False

# While loop so that the user has to keep entering their value if it isn't valid:
while integersCheck == False or from0to255Check == False:
    # Takes the user's input:
    denaryValue = input("Please enter an denary value between 0 and 255 inclusive, to be converted to 8-bit binary: ")
    # Checks if it contains only integers:
    numberOfIntegers = 0
    for counter in range(len(denaryValue)):
        if denaryValue[counter] >= "0" and denaryValue[counter] <= "9":
            numberOfIntegers = numberOfIntegers + 1
    if numberOfIntegers == int(len(denaryValue)):
        integersCheck = True
    else:
        print("Your value is not made up of only integers. ")
    # Checks if it is between 0 and 255 inclusive:
    numberOfIntegers = 0
    if int(denaryValue) >= 0 and int(denaryValue) <= 255:
        from0to255Check = True
    else:
        print("Your value is not between 0 and 255 inclusive. ")
# Informs the user that they have succeeded outside of the loop:
print("Your value is valid. ")

# Time to convert!

# Variables:
totalValueBinary = [0, 0, 0, 0, 0, 0, 0, 0]
leftoversAndScraps = 0
multiplier = 7

# Converts from denary to binary:
for positionInBinaryValue in range(8):
    if int(int(denaryValue @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@) - int(2) ** int(multiplier)) >= 0:
        leftoversAndScraps = int(leftoversAndScraps) + int(denaryValue) - int(2) ** int(multiplier)

        totalValueBinary[positionInBinaryValue] = 1
        print(totalValueBinary)

        multiplier = multiplier - 1

# Prints total outside of loop:
print("Your total value in denary is " + str(totalValueBinary) + ". ")