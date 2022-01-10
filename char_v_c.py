#Checking a Character is a vowel or consonant in Python
#Here, in this section we will discuss the program to check the entered character is a vowel or consonant in python. In Python string is an array representation of Characters python does not have a character data type.A single character is a string of length [1].
#Vowels:-
#A character is considered as a vowel when it belongs to the set of characters like{ ‘A’ , ‘E’ , ‘I’ , ‘O’ , ‘U’ }.

#Consonants:-
#A character is considered as consonant when the character belongs to any other alphabet then Set of Vowels.

#Example :    Input => A

#                      Output => A is a vowel

 #                     Input => R

  #                   Output => R is a consonant

#get user input
Char =  input() 
#Check if the Char belong to set of Vowels
if (Char == 'a' or Char == 'e' or Char == 'i' or Char == 'o' or Char == 'u'): 
    #if true 
    print("Character is Vowel") 
else: 
    #if false
    print("Character is Consonant")



