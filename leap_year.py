#Check Given Year is Leap Year or Not
#In this Python Program we have to find whether the year is a leap year or not.
 #In a year, there are only 365 Days but after every four year there are 366 days in a year. 
 #That is nothing but a leap year. The Gregorian calendar provides that a given year that is completely 
 #divisible by 100 (for example, 2000) is a leap year only if it is also completely divisible by 400.
 # leap year occurs for every 4 years feb 29th 

year=int(input())
if( (year%4==0 and year%100!=0) or year%400==0):
    print("leap")
else:
    print("not a leap year")    




