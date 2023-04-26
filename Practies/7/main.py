from solution import add_user, add_album, query_user_artist, query_user_genre, query_age_artist, query_age_genre, \
    query_city_artist, query_city_genre, all_users, all_albums

add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users, all_albums)
add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users, all_albums)
add_album("eclipse", "malmsteen", "classic", 10, all_users, all_albums)
add_album("barf", "beeptunes", "pop", 22, all_users, all_albums)
add_album("tekunbede", "beeptunes", "pop", 14, all_users, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_users, all_albums)

print(query_user_artist("SAliB", "sorena", all_users, all_albums))
print(query_user_artist("SAliB", "beeptunes", all_users, all_albums))
print(query_user_genre("SAliB", "pop", all_users, all_albums))
print(query_age_artist(22, "malmsteen", all_users, all_albums))
print(query_age_genre(19, "pop", all_users, all_albums))
print(query_city_artist("Tehran", "sorena", all_users, all_albums))
print(query_city_genre("Tehran", "pop", all_users, all_albums))
