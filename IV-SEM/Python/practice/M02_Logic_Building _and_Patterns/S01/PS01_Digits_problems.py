'''
sample input: 1234
sample output: 4

sample input: 12236
sample output: 5

to get last digit = number % 10

read a number from the user and display the no of digits in the number

num = int(input())
count = 0 # we use ount function to count the number of digits in the number.
while num > 0: 1
    count += 1 # count + 1 bcz we are counting the number of digits in the number.
    num = num // 10 # we use floor division to know the last digit from the number.
print(count)


# read input integers and give sum of digits in the number
num = int(input())
s = 0
while num>0:
    
    s += num % 10 
    num = num // 10 
  
print(s)

#read input and display all the even numbers in one line 

num = int(input())
while num > 0:  
    k = num % 10 
    if k % 2 == 0: 
        print(k, end = " ") 
    num = num // 10

#read a num from user and dispalay the reverse of the number
def reverse (num):
    rev = 0
    while num > 0:
        rev = (rev*10) + (num % 10)
        num = num // 10
    return rev  

n = reverse(int(input()))
while n > 0:
    d = n % 10
    if d % 2 == 0:
        print(d, end = " ")
    
    n = n // 10 
'''
# read a number from user and display palindrome , if yes then true no then false
#palindrome - a number which is same when read from left to right and right to left.

'''
1. count the number of digits in the number
2. sum of digits
3. reversing the number
4. even digits in the number
5.palindrome or not
6. check armstrong number or not - a number is called armstrong number if the sum of cubes of its digits is equal to the number itself.
ex - n = 123 so the cubes of 1 2 and 3 should be equal to 123
1^3 + 2^3 + 3^3 = 1 + 8
+ 27 = 36 which is not equal to 123 so 123 is not an armstrong number.
7.find largest num
8.find smallestnum
9. count zero digits 
10. find digital root of number - ex : n = 4653 , so the sum is 18 , but 18 is a double digit number so we again add 18 as 1 + 8 = 9 , now 9 is a single digit number . now we can display 9.

11. check spy number

'''

