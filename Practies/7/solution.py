all_users = {}
all_albums = {}


def add_user(username, age, city, albums, all_users, all_albums):
    all_users[username] = username


def add_album(album_name, artist_name, genre, tracks, all_users, all_albums):
    all_albums[album_name] = album_name


def query_user_artist(username, artist_name, all_users, all_albums):
    pass


def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    pass


def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    pass


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    pass


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    pass


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    pass

# DO NOT USE YOUR OWN TESTS HERE, USE SAMPLE TEST INSTEAD
