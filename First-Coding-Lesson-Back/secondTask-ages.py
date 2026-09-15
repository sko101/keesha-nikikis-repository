ages = []
for counter in range(5):
    addAColour = input("Please enter a colour (" + str(counter + 1) + "): ")
    ages.append(addAColour)
for counter in range(5):
    print("(" + str(counter + 1) + "): " + ages[counter] + ". ")