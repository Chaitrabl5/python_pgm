#Abundant Number:
#Python Program to check Abundant number. Abundant number is a number whose sum of the divisors of the number is
# greater than the number. To check for Abundant number, find and add the proper divisors of the number , 
 #compare the sum with the number if the sum is greater than the number then the number is an Abundant number
 # else not an Abundant number.  Diffrence between sum and the number is known as abundant.
#Example:
#12
#1*12
#2*6
#3*4
#1 + 2 + 3 + 4 + 6=16 > 12 (Abundant Number)
#21
#1*21
#3*7
#1 + 3 + 7=11 < 21 (Not an Abundant Number)


#enter the number to check
print('Enter the number:')

n=int(input())

sum=1 # 1 can divide any number 

for i in range(2,n):
  if(n%i==0):    #if number is divisible by i add the number 
   sum=sum+i

if(sum>n):
  print(n,'is Abundant Number')

else:
  print(n,'is not Abundant Number')