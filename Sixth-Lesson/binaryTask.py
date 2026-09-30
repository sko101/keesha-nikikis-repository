# Validity checks!

# Variables:
lengthCheck = False
integersCheck = False
binary0or1Check = False

# While loop so that the user has to keep entering their value if it isn't valid:
while lengthCheck == False or integersCheck == False or binary0or1Check == False:
    # Takes the user's input:
    binaryValue = input("Please enter an 8-bit binary value: ")
    # Checks if it is 8 characters in length:
    if int(len(binaryValue)) == 8:
        lengthCheck = True
    else:
        print("Your value does not have 8 characters. ")
    # Checks if it contains only integers:
    numberOfIntegers = 0
    for counter in range(len(binaryValue)):
        if binaryValue[counter] >= "0" and binaryValue[counter] <= "9":
            numberOfIntegers = numberOfIntegers + 1
    if numberOfIntegers == int(len(binaryValue)):
        integersCheck = True
    else:
        print("Your value is not made up of only integers. ")
    # Checks if it contains only 0s and 1s:
    numberOfIntegers = 0
    for counter in range(len(binaryValue)):
        if binaryValue[counter] == "0" or binaryValue[counter] == "1":
            numberOfIntegers = numberOfIntegers + 1
    if numberOfIntegers == int(len(binaryValue)):
        binary0or1Check = True
    else:
        print("Your value is not made up of only 0s and 1s. ")
# Informs the user that they have succeeded outside of the loop:
print("Your value is valid. ")

# Time to convert!

# Variables:
totalValueDenary = 0
multiplier = 7

# Converts from binary to denary:
for positionInBinaryValue in range(len(binaryValue)):
    if int(binaryValue[positionInBinaryValue]) == 1:
        totalValueDenary = int(totalValueDenary) + int(2) ** int(multiplier)
    multiplier = multiplier - 1
# Prints total outside of loop:
print("Your total value in denary is " + str(totalValueDenary) + ". ")