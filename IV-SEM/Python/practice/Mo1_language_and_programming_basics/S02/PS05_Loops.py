#loops types - for loop , while loop
#while loop - executes a block of code repeatedly as long as a condition is true.
#for loop - two types - range fun , iterable obj 
#range - range(start,stop,step)
#iterable obj - string , list , tuple , set , dictionary

'''
counter = 0
while counter < 5:
    print("hello world!")
    counter += 1  # counter = counter + 1   

read two integres start and stop variables.
display all the even numbers between start and stop (inclusive)
input : 1  10
output : 2 4 6 8 10


start = int(input())
stop = int(input())

for num in range(start, stop + 1):
    if num % 2 == 0:
        print(num, end=' ')

while start <= stop:
    if start % 2 == 0:
        print(start , end = '  ')
    start += 1


start = int(input())
stop = int(input())
while start <= stop:
    if start % 3 == 0 and start % 5 == 0:
        print("fizzbuzz")
    elif start % 3 == 0:
        print("fizz")
    elif start % 5 == 0:
        print("buzz")
    else:
        print(start)
    start += 1

#for loop
#syn: for i in range(start, stop, step):

for i in range(0, 3, 1):
    print("Hello world!")

#display n natural  numbers using for loop in the same line

n = int(input())
for i in range(1, n+1, 1): #why not n-1 bcz stop is excluded.so we use n + 1 for including n.We used 1 as step bcz we want to increment by 1
    print(i, end=' ')

# write the code to display natural numbers in reverse order using for order

n = int(input())
for i in range(n, 0,-1): #we used n,0,-1 bcz 0 as stop value , -1 as step to decrement by 1, n as start(it can be any natural number)
    print(i, end = ' ')
'''

li = [1,5,4,3,6,9,10]
for i in range(0,len(li),1):
    if i % 2 == 0:
        print(li[i], end = ' ') #output : 1 4 6 10

