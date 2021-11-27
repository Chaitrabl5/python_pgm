#Word Palindrome in Python
#Checking for word palindrome in Python is relatively easier. This is because there exists a built-in 
#function that reverses the sequences of a string – the reversed() function


#recieve an input from the user
input_word = input('Enter a word: ')

#reverse the word characters
reverse_word = ''.join(reversed(input_word))

#check if the word and reverse words are the same and print the corresponding output
if input_word.lower() == reverse_word.lower():
     print("The word is a palindrome!!!")
else:
    print("Unfortunately, this word is not a palindrome!!!")



