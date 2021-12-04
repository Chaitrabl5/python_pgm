#Python program to Check if the given number is Prime or not
#Prime numbers can only be divided evenly by 1 or itself, so these numbers are prime numbers.
#A few examples of such numbers are 2 , 3 , 5 , 7 , 11 , 13 , …………. and so on.

num=int(input())
if(num==2 | num==3|num==5|num==7):
    print("prime")
elif(num%2==0 or num%3==0 or num%5==0 or num%7==0):
    print("not prime")
else:
    print("prime")




