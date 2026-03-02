'''

factors nad multiples - prime numbers
prime numbers - number which is divisible by 1 and itself only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
take a number from the user and display all the factors of the number
input : 12
output: 1 2 3 4 6 12

n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end = " ")


#read a num from the uer and count the factors input - 12 , output - 6.
n = int(input())

count = 0 
for i in range(1, n+1):
    if n % i == 0:
        count += 1
print(count)


#write a program to check whether a number is prime or not
#input - 9 , output - not prime
n = int(input())
counter = 0
for i in range(2,n//2 + 1):
    if n % i == 0:
        counter += 1    
if counter == 0:
    print("prime")
else:
    print("not prime")

#using ternary
n = int(input("enter a number: "))
counter = 0
for i in range(2,n//2 + 1):
    if n % i == 0:
        counter += 1
print("prime" if counter == 0 else "not prime")

#print all the prime numbers in the given range , input- 1 10 , output - 2 3 5 7 11 13 17 19

num = int(input("enter a number: "))
for i in range(2, num+1):
    counter = 0
    for i in range(2, i//2 + 1):
        if i % j == 0:
            counter += 1
    if counter == 0:    
        print(i, end = " ") 
    
'''
#read a number from the user and display factorial of a number . Input - 5, output -120

n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0

n = int(input())
if n < 0:
    n = -1*n
    rev = int(str(n)[::-1])
    print(-1*rev)
else:
    print(int(str(n)[::-1]))






