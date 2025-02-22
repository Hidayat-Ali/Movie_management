# OOPS
## CREATE A MOVIE MANGEMENT SYSTEM THAT CAN MANAGE THE MOVIES AND BOOKINGS AND ALSO  
# CAN DISPLAY THE MOVIES WHICH ARE AVAIALBLE


# FUNCTIONALTIES
# Dispaly all the movies
# Book the movie
# Find the Movie in database 
# Cancel the Booking 

data = [
  {"movie_name":"Avengers","show_time":["10","12"],"available_seats":["20","30"]},
  {"movie_name":"krish","show_time":["10","12"],"available_seats":["20","30"]},
              
]

bookings=[]

def displayMovies():
    print(" \n All Movies ")
    for i in data:
        for key,value in i.items():
            print(f"{key},{value} \n")
        for time ,seat_avalaiblity in enumerate(i['show_time']):
            print(time)

        

            

            
    


displayMovies()








