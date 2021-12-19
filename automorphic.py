#Automorphic Number:
#In mathematics, an automorphic number (sometimes referred to as a circular number) is a natural number in a given number base b whose square end in the same digits as the number itself.

#Example:
 #n=25,
#25*25=625
#Output: Automorphic
#n=70,
#70*70=4900
#Output: Not Automorphic


n=int(input("Enter any number: "))
x=n**2
a=str(n)
b=str(x)
y=len(a)
z=len(b)
if(z-b.find(a)==y):
      print("Automorphic")
else:
      print("Not automorphic number")