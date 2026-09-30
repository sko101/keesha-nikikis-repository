def search(nameToSearch, list):
    index = 0
    found = False
    foundAt = 0
    while index < len(list) and found == False:
        if list[index] == nameToSearch:
            found = True
            foundAt = index
        index = index + 1
    return found, foundAt

names = ["Amir", "Beth", "Callum", "Dion"]
scores = [67, 81, 54, 72]

nameToSearch = input("Please enter a name to search for: ")
nameToSearch = nameToSearch.capitalize()
found, foundAt = search(nameToSearch, names)
if found == True:
    print("Student: " + str(nameToSearch) + ". Score: " + str(scores[foundAt]) + ". ")
else:
    print("Student's name not found. ")