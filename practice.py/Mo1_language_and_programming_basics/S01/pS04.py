"""
conditional statements in Python
1.if statement10
- having  only one possibilty , we use if statement
2.if...else statement
- having two possibilites , we use if...else statement
3.if...elif...else statement
- having more than two possibilites , we use if...elif...else statement

num1 = int(input("Enter a number:"))
if (num1 % 2 == 0):
    print("even number")
else :
    print("odd number")
"""
#check postive negative zero

num2 = int(input("Enter a number:"))
if(num2 > 0):
    print("positive number")
elif(num2 <0):
    print("negative number")
else:
    print("zero")




