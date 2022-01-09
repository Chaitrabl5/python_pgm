#Permutations In Which N People Can Occupy R Seats In A Classroom
#Here, we will discuss program for Permutations In Which N People Can Occupy R Seats in python .
# In this python program, we will be defining the number of ways in which N number of students can occupy
#  R number of seats. Take an example Ten friends enter the classroom late and all the seats are occupied by
#  toppers of the college and now only Six seats are available so in how many ways are those Ten friends will 
# occupy Six seats although 4 students have to leave the classroom. We will use math library for factorial 
# function in building of this program.

#import math lib
import math
#take user inputs
N = int(input('Enter the number of students :'))
R = int(input('Enter the number of seats :'))
#factorial by using factorial() function
nume = math.factorial(N)
deno = math.factorial(N-R)
#permutation = n! / (n-r)!
no_of_ways = nume//deno
#print total no of ways
print('Total number of ways are :' + str(no_of_ways))

