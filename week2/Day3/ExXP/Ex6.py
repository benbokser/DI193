# 🌟 Exercise 6: Birthday and minutes

# Key Python Topics:

#     datetime module
#     datetime.datetime.strptime() (parsing dates)
#     Time difference calculations
#     .total_seconds() method


# Instructions:

# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
import datetime as dt
def show_minutes_lived(birthdate: str):
    birth_datetime = dt.datetime.strptime(birthdate, "%B %d, %Y")
    current_date_and_time = dt.datetime.now()
    time_lived = current_date_and_time - birth_datetime
    minutes_lived = time_lived.total_seconds() / 60
    print(f'User has lived {minutes_lived} minutes')

show_minutes_lived('March 3, 1995')