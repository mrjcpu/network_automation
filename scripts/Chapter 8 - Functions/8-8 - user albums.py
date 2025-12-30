def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary with information about the album"""
    album = {
        'artist':artist_name,
        'title':album_title
    }

    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    return album

while True:
    print(f"\nPlease enter the album information:")
    print("(Enter 'quit' to exit)")

    artist = input("Artist Name: ")
    if artist.lower() == 'quit':
        break
    album = input("Album Name: ")
    if album.lower() == 'quit':
        break
    songs = input("Number of Songs: ")
    if songs.lower() == 'quit':
        break

    full_album = make_album(artist, album, songs)
    print(full_album)



