'''
create an empty list and traverse through empty list
li = [ 1,2,3,4,5] , output - [1,4,9,16,25]


li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i**2)
print(res)

ans = [i ** 2 for i in li] 
print(ans)

input - [1,2,3,4,5] output;[2,4]

li = [1,2,3,4,5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

ans =[i for i in li if i % 2 == 0] 
print(ans)


print(" * "*5)
join multiple strings as a single string using join, + operator, and f string, format method.

li = ['a','b','c'] # output - 'a b c'
res =""
for ch in li:
    res = res + ch +" " # res + ch = 'a' + 'b' + 'c' = 'abc'
print(res)

" ".join(li) # we use join method to join the strings as a single string.
print(" @ ".join(li))
 
1. pyramid
n = 4
output :
 
display pyramid patterm using a single loop
   *
  * *
 * * *
* * * *

n = int(input())
for i in range(1 , n+1):          
    print(" " *(n-i)+"* "*i)

# 2.inverted pyramid

n = int(input())
for i in range(n,0,-1):
    print(" " *(n-i)+"* "*i)

#3.Diamond patterns

n = int(input())
for i in range(1 , n+1):          
    print(" " *(n-i)+"* "*i)

for i in range(n-1,0,-1):
    print(" " *(n-i)+"* "*i)
'''
# 4.number pyramid
#n=4
#output - 
#   1
#  1 2
# 1 2 3 
#1 2 3 4

n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) +" ".join([str(j) for j in range(1,i+1)])) # we used this line to explain the list comprehension and join method and range function and string formatting.

#5 . palindrome pattern
#6 . reverse number triangle
#7. binary triangle n = 4
#8. cross pattern n =5 
#9. Hollow daimond n = 4
#10. hollow pyramid n = 4
# construct a hollow pyramid n = 4
#   *
#  * *
# *   *
#*******

n = int(input())
for i in range(1, n+1):
    print(" "*(n-i)+"* "*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*(2*i-1))





