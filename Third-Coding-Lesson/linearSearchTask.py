# ages = [1, 2, 3, 89, 99, 5, 14, 7, 6]
# index = 0
# found = False
# indexWhereFound = 0
# valueToBeSearchedFor = int(input("Please enter a number to be searched for: "))
# while index < len(ages) and found == False:
#     if ages[index] == valueToBeSearchedFor:
#         found = True
#         indexWhereFound = index
#     index = index + 1
# if found == True:
#     print("The value was found at position " + str(indexWhereFound - 1) + " (index " + str(indexWhereFound) + "). ")
# else:
#     print("The value was not found. ")


def linearSearch(valueToBeSearchedFor, list):
    index = 0
    found = False
    indexWhereFound = 0
    while index < len(list) and found == False:
        if list[index] == valueToBeSearchedFor:
            found = True
            indexWhereFound = index
        index = index + 1
    if found == True:
        print("The value was found at position " + str(indexWhereFound - 1) + " (index " + str(indexWhereFound) + "). ")
    else:
        print("The value was not found. ")


list = [1, 2, 3, 89, 99, 5, 14, 7, 6]
valueToBeSearchedFor = int(input("Please enter a number to be searched for: "))
linearSearch(valueToBeSearchedFor, list)