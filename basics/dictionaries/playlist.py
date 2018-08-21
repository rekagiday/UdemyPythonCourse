playlist = dict(
    title = 'happy',
    author = 'Reka',
    songs = [
        {'title': 'Zombie', 'artist': ['Jamie T'], 'album': 'Carry On The Grudge', 'length': 2.30 },
        {'title': 'Love Is All I Got', 'artist': ['Feed Me', 'Crystal Fighters'], 'album': 'Love Is All I Got', 'length': 3.40 },
        {'title': 'Easy Money', 'artist': ['Johnny Marr'], 'album': 'Playland', 'length': 4.12 },
    ]
)


# playlist length
total_length = 0.0
for song in playlist['songs']:
    total_length += song.get('length')

print(playlist)
print(f"total length of playlist {playlist['title']}: {total_length}")
