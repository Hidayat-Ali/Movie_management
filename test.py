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

# 1: functional programing 2 : Object oriented programmig  3: Asynchronous Programming 


# bookings=[]

# def displayMovies():
#     print(" \n All Movies ")
#     for i in data:
#         for key,value in i.items():
#             print(f"{key},{value} \n")
#         for time ,seat_avalaiblity in enumerate(i['show_time']):
#             print(time)



#my code


# movies_database = [
#    { "movie_name" : "Tare zameen par", "show_time" : ["10.55", "08.30"], "price_ticket" : "500", "available_seats": 20},
#    {"movie_name": "Chicichore", "show_time": ["01.55", "02.30"], "price_tic": "500", "availble_seats" :  80},
# ]



 



def displaymovies():
    print("\n All Movies")
    for movie in movies_database:
        # what to write here
        print(movie['movie_name'])
        print("ticket price",movie['price_ticket'])
        for index,time in enumerate(movie["show_time"]):
            print('show time',time)
            print('available seats',movie['available_seats'][index])
        # for index,seats in enumerate(movie['available_seats']):
        #     print('availble seats',seats)
    
        print(".............")



# displaymovies()





    # for movie in allmovies:
    #     search = input("Enter the moveie you want to search: ")
    #     if search == movie:
    #         print("The movies is there")
    #         break
    #     else:
    #         print("Movie does not exist")
    #         break


# search_movie()

# displayMovies()

