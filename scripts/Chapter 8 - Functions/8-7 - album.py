def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary with information about the album"""
    album = {'artist':artist_name, 'title':album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

album = make_album('jimi hendrix', 'electric ladyland',number_of_songs=3)
print(album)

album = make_album('50 Cent', 'Power of a Dollar')
print(album)

album = make_album('Miles Davis', 'Rebirth of Cool',number_of_songs=19)
print(album)
