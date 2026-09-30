def search(valueToSearch, list):
    index = 0
    found = False
    timesFound = 0
    while index < len(list):
        if list[index] == valueToSearch:
            found = True
            timesFound = timesFound + 1
        index = index + 1
    return found, timesFound

numbers = [5, 8, 5, 3, 5, 9, 5]
valueToSearch = int(input("Please enter a value to search for: "))
found, timesFound = search(valueToSearch, numbers)
if found == True:
    if timesFound == 1:
        print("The value was found " + str(timesFound) + " time. ")
    else:
        print("The value was found " + str(timesFound) + " times. ")
else:
    print("Value was not found. ")