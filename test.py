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

# movies_database = [
#    { "movie_name" : "Tare zameen par", "show_time" : ["10.55", "08.30"], "price_ticket" : "500", "available_seats": 20},
#    {"movie_name": "Chicichore", "show_time": ["01.55", "02.30"], "price_tic": "500", "availble_seats" :  80},
# ]




# # def displaymovies():
# #     print("\n All Movies")
# #     for i in movies_database:

# #         for key, value in i.items():
# #            print(f"{key}, {value} \n")

# #         for time,seat in enumerate(i["show_time"]):
# #             print(time)

# #         print(".............")



# # displaymovies()




# #search movie

# def search_movie():
#     allmovies =[]
#     for i in range(len(movies_database)):
#         a = movies_database[i]["movie_name"]
#         allmovies.append(a)

#     for movie in allmovies:
#         search = input("Enter the moveie you want to search: ")
#         if search == movie:
#             print("The movies is there")
#             break
#         else:
#             print("Movie does not exist")
#             break


# search_movie()


#book movie



movies_database = [
    {"movie_name" : "Tare Zameen par", "price_ticket" : 500  , "show_time" : ["10.30", "12.30"], "available_tickets" : [10,20]},
    {"movie_name" : "Krish", "price_ticket" : 900, "show_time" : ["10.56", "08.30"], "available_tickets" : [10,40]} 
    ]



#DISPLAY ALL MOVIES
def displaymovies():
    print("\n All Movies")
    for movie in movies_database:
        print("Movies_Name:", movie["movie_name"])
        print("Ticket_Movie:", movie["price_ticket"])
        
        for index, time in enumerate(movie["show_time"]):
            print("Timing:", time)
            print("Avaible Seats", movie["available_tickets"][index])

        print("................")


#displaymovies()



#BOOK MOVIE
def book_movie():

    for movie in movies_database:
        input_movie = input("Enter the movie you want to watch: ")


        if input_movie == movie["movie_name"]:
            print("Yes Movie is here"
            print("Book the ticket")
            break
        else:
            print("No Movie is not here")


book_movie()
        

        




