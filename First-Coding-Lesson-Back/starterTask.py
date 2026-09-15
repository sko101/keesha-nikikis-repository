# names = ["Muskaan", "Keesha Nikiki herself", "Liyana", "Devansshi", "Maggie", "Elizabeth", "Jessie", "Saymeen", "Vigdis", "Laya", "Debbie"]
# for counter in range(len(names)):
#     print(len(names[counter]))
# getName = input("Please, if you would be so kind, could you potentially, maybe enter a name?: ")
# names.append(getName)
# print(names)

colours = []
for counter in range(3):
    addAColour = input("Please enter a colour (" + str(counter + 1) + "): ")
    addAColour = addAColour.capitalize()
    colours.append(addAColour)
for counter in range(3):
    print("(" + str(counter + 1) + "): " + colours[counter] + ". ")