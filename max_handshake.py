#Maximum Number Of Handshakes in Python
#Here, in this page we will discuss the program to find the maximum number of handshakes in python.

#For the number of handshakes to be maximum, every person should shakehand with every 
# other person in the room i.e all persons present should shake hands. For the first person, 
# there would be N-1 people to shake hands. For second person there would N-1 people available 
# but as he had already shaken hands with the first person,  there would be N-2 people to shake 
# hands and so on.

#Therefore the total number of handshake = (N-1 + N-2 +….+ 1 + 0)=((N-1)*N)/2.
#take user inputs
N = int(input('Enter number of people available :'))
#formula
no_of_handshakes = int(N *((N-1)/2))
#print number of no_of_handshakes
print('Maximum number of handshakes can be :' + str(no_of_handshakes))

