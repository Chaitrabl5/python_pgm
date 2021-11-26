#Fibonacci series in python is a sequence of numbers in which the current term is the sum of 
# the previous two terms.
# The first two terms of the Fibonacci sequence are 0 and 1

def fib(n):
    count=0
    n1,n2=0,1
    arr=[]
    while count<n:
        arr.append(n1)
        nf=n1+n2
        n1=n2
        n2=nf
        count+=1
    return arr    

num=int(input("enter a number"))
res=fib(num) 
   
print(' '.join(map(str, res)))