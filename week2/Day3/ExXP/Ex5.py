# 🌟 Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.


# Instructions:
# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module
import datetime as dt
# Step 2: Get the current date and time
current_date_and_time = dt.datetime.now()
# Step 3: Create a datetime object for January 1st of the next year
upcoming_jan_1 = dt.datetime(2027, 1, 1)
# Step 4: Calculate the time difference
time_diff = upcoming_jan_1 - current_date_and_time
# Step 5: Display the time difference
print(time_diff)