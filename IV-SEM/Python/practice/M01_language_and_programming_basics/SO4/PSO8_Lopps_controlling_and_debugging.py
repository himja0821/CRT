'''
types errors: 
1.syntax error - error in the syntax of the program. ex: missing colon, indentation error etc.
2.runtime eerors - error during execution of the program.ex: division by zero, file not found etc.
3.logical errors - program runs successfully but output is not as expected. ex: wrong formula, wrong condition etc.

debugging of errors: 
1. print fucntion - using print statements to check the values of variables at different points in the program.
2.Using pdb module - python debugger module
pdb commands :
n - execution in next line.
p var - print value of var.
l - list nearby code
c - continue execution until next breakpoint.
s - step into function call.
r - return from the fucntion
q - quit the debugger
h - help
3.try and except block - to handle runtime errors and prevent program from crashing. 
himaja

try:
    a = int(input("enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("division by zero is not allowed")
except ValueError:
    print("invalid input")
'''
# execute the code using pdb. Addition between two numbers.
import pdb

def add(a,b):
    pdb.set_trace() 
    return a + b
a = int(input("enter a number:"))
b = int(input("enter another number:"))
print(add(a,b))



