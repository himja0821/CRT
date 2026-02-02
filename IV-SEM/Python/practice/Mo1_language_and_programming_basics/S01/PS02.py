"""
Datatypes for python
1.fundamentaldt
    1integer - without decimal point
    2.float - num with decimal points
    3.complex - a+bj -> a(real part) b(imaginary part)
    4.boolean type - True/False
    5.string type - collection of characters enclosed in single/double/triple quotes , immutable 
2.connection dt
    1.list
    2.tuple
    3.set
    4.dictionary

x = 10
y = 20.5
z = 3 + 4j
a = True
print(type(x)) #type function - used to determine 
print(type(y))
print(type(z))
print(type(a))
f1 = 12e2   #float numbers can be represented in floating point and alphabets e nd E
f2 = 5E3
print(f1 , type(f1))
print(f2 , type(f2))

c1 = 5 +4j
c2 = complex(2 ,-3)
print(c1,c2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.real) # gives real part
print(c1.imag) # gives imaginary part

s1 = "python"
s1 = 'python programming'
s3 = '''python 3.14.2'''
s4 = '''line-1  # these three lines are considered as string creations
line-2
line3
'''

s1 = "python"
print(s1[1:5:1]) #slicing operation: [start,stop,stepsize] - stop index is excluded.
print(s1[3]) #'h'
print(s1[::2]) #pto
print(s1[::-1]) #reverse the string
"""
s2 = 'programming'
print(s2[2:7:2])

