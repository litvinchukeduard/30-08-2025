from enum import Enum, auto

#GENRES = ["Dance", "Rock", "Pop"]

class SongGenres(Enum): # Enumerated (Enumeration)
    DANCE = auto()
    POP_2 = auto()
    ROCK = auto()
    POP = auto()


# print(SongGenres.POP_2)
genre = SongGenres.POP
if genre == SongGenres.ROCK:
    print("this is a rock song")
elif genre == SongGenres.POP:
    print("this is a pop song")
elif "Hello" == "World":
    ...
match genre:
    case SongGenres.POP:
        print('This is a pop song')
    case SongGenres.ROCK:
        print('This is a rock song')
    case SongGenres.DANCE:
        print('This is a dance song')


# set_one = {"a", "b", "c"}
# # set_one.add("a")
# print(set_one)

# my_list = [1, 2, 4]
# print(3 in my_list)

# for element in {1, 2, 3}:
#     print(element)

# [1, 2, 3][0]

# my_list = [1, 2, 3]
# my_list[1] = "Hello"
# print(my_list + [4, 5, 6])
