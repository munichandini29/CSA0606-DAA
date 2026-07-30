# Playlist Reordering using Insertion Sort

n = int(input("Enter number of songs: "))
playlist = []

for i in range(n):
    name = input("Enter song name: ")
    duration = int(input("Enter duration (seconds): "))
    playlist.append([name, duration])

for i in range(1, n):
    key = playlist[i]
    j = i - 1

    while j >= 0 and playlist[j][1] > key[1]:
        playlist[j + 1] = playlist[j]
        j -= 1

    playlist[j + 1] = key

print("\nSorted Playlist:")
for song in playlist:
    print(song[0], "-", song[1], "seconds")
