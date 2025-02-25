movies_database = [
   { "movie_name" : "Tare zameen par", "show_time" : ["10.55", "08.30"], "price_ticket" : "500", "available_seats": "20"},
   {"movie_name": "Chicichore", "show_time": ["01.55", "02.30"], "price_tic": "500", "availble_seats" :  "80"},
]


def displaymovies():
    print("\n All Movies")
    for i in movies_database:
        for key, value in i.items():
            print(f",{key}, {value} \n")

        print(".............")



displaymovies()
