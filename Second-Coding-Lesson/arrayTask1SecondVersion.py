songs = [
    ["Cicada", "Wall", "Drifting", "Something-Anything", "Televisional", "Pool House", "its alright :) (E)", "Meet Me in the Middle", "I'm Not Crazy", "Monodrama", "Televised", "Porch Light"],
    ["Good kid", "Good kid", "Good kid", "Pretoria", "Pretoria", "The Backseat Lovers", "Cafune", "Kevin Walkman", "Kevin Walkman", "Kevin Walkman", "benches", "Rebounder", "almost monday", "HUNNY", "Ally Evenson"]
]

print(str(songs[0][0]) + " - " + str(songs[1][0]))
print(str(songs[0][2]) + " - " + str(songs[1][2]))
print(str(songs[c[len(songs) - 1]) + " - " + str(songs[len(songs) - 1][1]))

getSecondSongReplacement = input("What would you like to replace the second song with?: ")
songs[1][0] = getSecondSongReplacement
getSecondSongReplacement = input("What would you like to replace the second artist with?: ")
songs[1][1] = getSecondSongReplacement
print(songs[1])

for counter in range(len(songs)):
    print(str(counter + 1) + ": " + str(songs[counter]))

print("There are " + str(len(songs)) + " songs in this playlist. ")