from dataclasses import dataclass
from collections import UserList
'''
Система керування піснями

Лише зберігає інформацію про пісні


Song (author, name, duration_in_seconds)

Playlist

list (choose list, але потрібно буде додати перевірку на унікальність)
set
'''


# class Song:
#     def __init__(self, author: str, name: str, duration_in_seconds: int):
#         if author is None or len(author) == 0:
#             raise ValueError('Author name can not be empty')
#         self.author = author
#         self.name = name
#         self.duration_in_seconds = duration_in_seconds


class PlaylistError(ValueError):
    ...


class DuplicateSongInPlaylistError(PlaylistError):
    ...


class PlaylistIsTooLongError(PlaylistError):
    ...


class PlaylistElementIsNotASong(PlaylistError):
    ...


@dataclass
class Song:
    author: str
    name: str
    duration_in_seconds: int

    def __post_init__(self):
        if self.author is None or len(self.author) == 0:
            raise ValueError('Author name can not be empty')
        

class Playlist(UserList):

    def check_if_element_is_valid(self, element):
        if not isinstance(element, Song):
            raise PlaylistElementIsNotASong("Element added is not a song")
        if element in self.data:
            raise DuplicateSongInPlaylistError('This song already exists in this playlist')
        if len(self.data) + 1 > 2:
            raise PlaylistIsTooLongError('Playlist can not be longer than 2')

    def append(self, song):
        self.check_if_element_is_valid(song)
        return super().append(song)

if __name__ == '__main__':
    song_one = Song('Author One', 'Song One', 300)
    print(song_one)
    print(song_one.author)
    print(song_one.duration_in_seconds)

    my_list = []
    my_list.append(song_one)
    my_list.append(song_one)
    my_list.append(song_one)
    print(my_list)

    playlist = Playlist()
    try:
        playlist.append(song_one)
        playlist.append(1)
        # playlist.append("Hello")
        # playlist.append([1, 2, 3])
    
    except PlaylistIsTooLongError:
        print("This playlist is too long")
    except DuplicateSongInPlaylistError:
        print("You have a duplicate song in your playlist")
    except PlaylistElementIsNotASong:
        print("Element added to the playlist is not a song")
    except PlaylistError:
        print('Something is wrong with the playlist')
    except ValueError:
        print('ValueError happened')
    
    
    for song in playlist:
        print(song)

    
