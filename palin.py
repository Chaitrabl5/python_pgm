#Palindrome or not
#A palindrome number means reverse of a number and original number both are equal. 
#First we have to find the reverse of a number using while loop and else if statement. Then we will check condition, if original number is equal to the reverse of a number. For Example:-
#A number is 526625 .If you read number “526625” from reverse order, 
#it is same as “526625”.  Hence the number is palindrome
num = int(input("Enter the Number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

if temp == reverse:
    print("Given number {} is Palindrome".format(temp))
else:
    print("Given number {} is not Palindrome".format(temp))
    