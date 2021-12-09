#Find Fibonacci series up to n
#In this Python Program, We will be finding n number of elements of a Fibonacci series. 
#Fibonacci Series are those numbers which are started from 0, 1 and their next number is the sum of the previous
 #two numbers. So, First few Fibonacci series elements are 0,1,1,2,3,5,8,13 and so on. 
 #This program will ask one user input and then it will print that n number of elements of Fibonacci series.

#For Example:

#Limit is Fibonacci series : 10

#Sequence is 0,1,1,2,3,5,8,13,21, 34

def fibonacciSeries(i):
    if i <= 1:
       return i
    else:
          return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num=int(input("Enter a number: "))
if num <=0:
     print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
    for i in range(num):
           print(fibonacciSeries(i), end=" ")

