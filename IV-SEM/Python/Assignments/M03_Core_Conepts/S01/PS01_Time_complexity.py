'''
Time complexity - time required to run an algo based on inputs.
1. O(1) - constant time
2. O(n) - linear time
3. O(n ^ 2) - quadratic time
4. O(log n) - logarithmic time
5. O(nlogn) - linwarthimic time
6. O(2^n)- exponential time  

'''
def constant_time(arr):
    return arr[0]
print(constant_time[10, 20, 30]) #O(1)

def Quadratic_Time(arr):
    for i in arr:
        for j in arr:
            print(i)
print(Quadratic_Time[10, 20, 30, 40, 50]) # O(n^2)

def linearthimic_time(arr):
    return sorted[0]
print(linearthimic_time[10,20, 30, 20, 50, 20])  #O(nlogn)

def fibo(n):
    if n<=1:
        return n 
    return fibo(n-1)+fibo(n-2)

n = int(input())
print(fibo(n)) #0(2^n)


