# Exercise 2 : How Old Are You On Jupiter?
# Instructions

#     Given an age in seconds, calculate how old someone would be on all those planets :
#         Earth: orbital period 365.25 Earth days, or 31557600 seconds
#             Example : if someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.
#         Mercury: orbital period 0.2408467 Earth years
#         Venus: orbital period 0.61519726 Earth years
#         Mars: orbital period 1.8808158 Earth years
#         Jupiter: orbital period 11.862615 Earth years
#         Saturn: orbital period 29.447498 Earth years
#         Uranus: orbital period 84.016846 Earth years
#         Neptune: orbital period 164.79132 Earth years
earth_yr = 31557600 #seconds
# planet_age = seconds/planet_yr (in seconds)
def earth_age(seconds):
    return seconds/earth_yr
# 1 earth yr = earth_yr seconds
# 1 merc_yr = 0.24... earth yrs = 0.24...(earth_yr) seconds
# merc_age = seconds/(0.24...*earth_yr
# 4 merc_yr = 1 earth_yr = earth_yr seconds
def mercury_age(seconds):
#         Mercury: orbital period 0.2408467 Earth years
    return seconds / (0.2408467* earth_yr)

print(mercury_age(315576000))

