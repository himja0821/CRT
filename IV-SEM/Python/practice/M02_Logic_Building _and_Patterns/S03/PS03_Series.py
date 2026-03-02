'''
series - sequence of numbers which follow a particular pattern.
fibanocci series - 0 amd 1 , sum of two previous numbers. like 0 , 1,1,2,3,5,8,13,21,34,55,89.

arithmetic series:
input : 1   2
output : 1 3 5 7 9 11 13 15 17 19

a = int(input())
b = int(input())
for i in range(10): #we took 10 bcz we want to print 10 numbers in the series.
    print(a + i* b , end= " ")

    
wap on geometric series:
1 2 


a = int(input())
b = int(input())
for i in range(10):
    print(a*(b**i), end = " ") 

Fibanocci series: read a number from the user and display the fibanocci series till that number.

#traditionalway
n = int(input())
a = 0
b = 1
while a <= n:
    print(a, end = " ")
    a , b = b , a + b # we are swapping the values of a and b and then adding them to get the next number in the series.


li = [0,1]
for i in range(2,n):
    li.append(li[i-1] + li[i-2]) # we are adding the last two numbers in the list to get the next number in the series.
print(li)

factorial of a number
'''
n = int(input())
if n < 0:
    print("No factorial for -ve")
elif n == 0 or n == 1:
    print("1")
else:
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)

