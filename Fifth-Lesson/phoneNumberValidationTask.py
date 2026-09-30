valid = False
lengthCheck = False
integersCheck = False
beginningCheck = False
while valid == False:
    phoneNumber = input("Enter a phone number: ")
    if len(phoneNumber) == 11:
        lengthCheck = True
    else:
        print("Your phone number is not 11 characters. ")
    numberOfIntegers = 0
    for counter in range(len(phoneNumber)):
        if phoneNumber[counter] >= "0" and phoneNumber[counter] <= "9":
            numberOfIntegers = numberOfIntegers + 1
    if numberOfIntegers == int(len(phoneNumber)):
        integersCheck = True
    else:
        print("Your phone number is not made up of integers. ")
    if str(phoneNumber[0]) + str(phoneNumber[1]) == "07":
        beginningCheck = True
    else:
        print("Your phone number does not begin with 07. ")
    if lengthCheck == True and integersCheck == True and beginningCheck == True:
        valid = True
print("Thank you for your valid phone number. ")