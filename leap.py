#A leap year is a year that has 366 days rather than 365 days. 

#A year is a leap year if:
#It has 366 days 
#The year is divisible by 4. 
#Is a centurion year and is divisible by 400. 
#It is important to point out that centurion years are not leap years if they are not divisible by 400.

def check_leap_year():
    #allow user input the year
    year = int(input('Entire the year you wish to check: '))
    
    #define the conditions
    if year % 400 == 0:
        return(f"Yes, {year} is a leap year")
    if year % 100 == 0:
        return(f"No, {year} is not a leap year")
    if year % 4 == 0:
        return(f"Yes, {year} is a leap year")
    return(f"No, {year} is not a leap year")