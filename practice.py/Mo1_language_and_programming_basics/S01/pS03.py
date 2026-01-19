"""
Operators in python
1.unary - operates on a single operand
2.binary - operates on two operands
3.ternary - operates on three operands
operators: arithmetic (+,-,*,%,//,**), assignment(=,+=,-=,*=,/=,//=,**=,%=),
comparison(==,!=,>,<,>=,<=), logical(and,or,not),
bitwise(&,|,^,~,<<,>>), membership(in,not in), identity(is,is not)
bitwise - &:
    1 & 0 = 0
    0 & 1 = 0
    1 & 1 = 1
    0 & 0 = 0
bitwise - |:
    1 | 0 = 1
    0 | 1 = 1
    1 | 1 = 1
    0 | 0 = 0
bitwise - ^:
    1 ^ 0 = 1
    0 ^ 1 = 1
    1 ^ 1 = 0
    0 ^ 0 = 0
bitwise - ~:
    ~x = x
bitwise - <<:

x = 13
print(x << 2)
print(x >> 2)

membership : in , not in - bool type. (in --> keyword)
-used to check whether a value/variable is present in a sequence (list,tuple,set,dictionary,string) or not.

identity :is , is not -bool type .

x = 10
y = 20
z = 10
print( x is y) #false
print(x is z) #true
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2) #false

memory management in python - stack and heap memory
stack - small in size, faster access, stores primitive dt and references to objects in heap
heap - large in size, slower access, stores objects of dt (dt - datatype)

refernce algorithm - used to manage memory in python

"""
x = 2
y = 5
z = 40
print("arithemtic operators")
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)
print("x ** y =", x ** y)

print("assignment operators")
x += 3  
print("x += 3 ->", x)
y -= 2      
print("y -= 2 ->", y)
z *= 4
print("z *= 4 ->", z)



