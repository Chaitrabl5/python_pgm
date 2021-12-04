#A program to check if a number is a prime number or not
#recieve an input from the user
number = int(input('Enter a positive number: '))

#check if its a prime number
if number>1:
    for numbers in range(2, number):
        if (number % numbers) ==0:
            print(f"{number} is not a prime number")
         
            break
    else:
        print(f"{number} is a prime number")  
else:
    print(f"{number} is not a prime number")