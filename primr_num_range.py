#A python program to print all the prime numbers within an interval of numbers

#create an interval for the range of numbers
lower_number = int(input('Enter the lower limit: '))
upper_number = int(input('Enter the upper limit: '))
prime_num = []

#Then, we use for loop to produce the prime numbers
for i in range(lower_number, upper_number +1):
    if i >1:
        for j in range(2, i):
            if (i %j) ==0:
                break
        else:
            prime_num.append(i)

print(f"The prime numbers between {lower_number} and {upper_number} are {prime_num}")