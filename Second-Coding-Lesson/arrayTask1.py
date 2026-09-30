songs = ["Cicada - Good kid",
         "Wall - Good kid",
         "Drifting - Good kid",
         "Something-Anything - Pretoria",
         "Televisional - Pretoria",
         "Pool house - The Backseat Lovers",
         "e-Asphyxiation - Cafune",
         "its alright :) - Kevin Walkman",
         "Meet Me in the Middle - Kevin Walkman",
         "I'm Not Crazy - Kevin Walkman",
         "Monodrama - benches",
         "Japanese Posters - Rebounder",
         "can't slow down - almost monday",
         "Televised - HUNNY",
         "Porch Light - Ally Evenson",
         ]

print(songs[0])
print(songs[2])
print(songs[len(songs) - 1])

getSecondSongReplacement = input("What would you like to replace the second song with?: ")
songs[1] = getSecondSongReplacement
print(songs[1])

for counter in range(len(songs)):
    print(str(counter + 1) + ": " + str(songs[counter]))

print("There are " + str(len(songs)) + " songs in this playlist. ")