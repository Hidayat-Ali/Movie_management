# OOPS
## CREATE A MOVIE MANGEMENT SYSTEM THAT CAN MANAGE THE MOVIES AND BOOKINGS AND ALSO  
# CAN DISPLAY THE MOVIES WHICH ARE AVAIALBLE


# FUNCTIONALTIES
# Dispaly all the movies
# Book the movie
# Find the Movie in database 
# Cancel the Booking 

# data = [
#   {"movie_name":"Avengers","show_time":["10","12"],"available_seats":["20","30"]},
#   {"movie_name":"krish","show_time":["10","12"],"available_seats":["20","30"]},
              
# ]

# bookings=[]

# def displayMovies():
#     print(" \n All Movies ")
#     for i in data:
#         for key,value in i.items():
#             print(f"{key},{value} \n")
#         for time ,seat_avalaiblity in enumerate(i['show_time']):
#             print(time)

        

            

            
    


# displayMovies()





#my code

movies_database = [
   { "movie_name" : "Tare zameen par", "show_time" : ["10.55", "08.30"], "price_ticket" : "500", "available_seats": 20},
   {"movie_name": "Chicichore", "show_time": ["01.55", "02.30"], "price_tic": "500", "availble_seats" :  80},
]




def displaymovies():
    print("\n All Movies")
    for i in movies_database:

        for key, value in i.items():
           print(f"{key}, {value} \n")

        for time,seat in enumerate(i["show_time"]):
            print(time)

        print(".............")



displaymovies()




#search movie

def search_movie(search):
    allmovies =[]
    for i in range(len(movies_database)):
        a = movies_database[i]["movie_name"]
        allmovies.append(a)

    for movie in allmovies:
        search = input("Enter the moveie you want to search: ")
        if search == movie:
            print("The movies is there")
        else:
            print("Movie does not exist")


search_movie(Patrner)





#book movie
