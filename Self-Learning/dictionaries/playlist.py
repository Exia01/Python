playlist = {
	'title': 'patagonia bus', 
	'author': 'Kal DJ', 
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
	]
}

# total_length = 0
# for song in playlist['songs']:
# 	total_length += song['duration']

# for value in playlist['songs']:
#     print(value['title']) 

total_length = sum([song.get('duration', 0) for song in playlist['songs']])

print(total_length)