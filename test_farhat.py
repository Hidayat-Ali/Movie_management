movies_database = [
   { "movie_name" : "Tare zameen par", "show_time" : "10.55", "price_ticket" : 500, "available_seats": ["20","30"]},
   {"movie_name": "Chicichore", "show_time": "09.00", "price_tic": 500, "availble_seats" : ["40", "32"]},
]


def displaymovies():
    print("\n All Movies")
    for i in movies_database:
        for key, value in i.items():
            print(f"{key}, {value} \n")

displaymovies()