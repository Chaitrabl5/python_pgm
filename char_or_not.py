#Checking whether a Character is Alphabet or Not in Python ?
#Here, we will discuss program to check whether a Character is alphabet or not in python .All characters whether alphabet, digit or special character have ASCII value. Input character from the user will determine if it’s Alphabet, Number or Special character. 

#Alphabets (a, b, c… )
#Digits(1, 2, 3…)
#Special characters(@, %, &…)
#ASCII value ranges-

#For capital alphabets 65 – 90
#For small alphabets 97 – 122
#For digits 48 – 57
#All other cases are Special Characters. 

#Example: 

#Input : 4
#Output : Not an Alphabet
#Input : A
#Output : Alphabet

n=input() 

#ASCII value of the input 

x=ord(n)

if(65<=x<=90 or 97<=x<=122):

    print('yes' , n , 'is an Alphabet')

else:

    print('No' , n , 'is not an Alphabet')



