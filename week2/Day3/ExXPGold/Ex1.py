# Exercise 1 : Upcoming Holiday
# Instructions

#     Write a function that displays today’s date.
#     The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is New Years’ Eve in 30 days).
#     Hint: Use a module to find the datetime and name of the upcoming holiday.

import datetime as dt
import holidays

def get_next_holiday(country_code='US'):
    # Get all holidays for the current and next year (to handle December)
    current_year = dt.date.today().year
    geo_holidays = holidays.country_holidays(country_code, years=[current_year, current_year + 1])
    
    # Sort dates and find the first one that is >= today
    today = dt.date.today()
    upcoming = sorted((d, name) for d, name in geo_holidays.items() if d >= today)
    print(dt.date.today())
    next_holiday = (upcoming[0] if upcoming else None)
    time_until = (next_holiday[0] - dt.date.today()).days
    print(f'The next holiday is {next_holiday}, which is {time_until} days away.')
get_next_holiday()