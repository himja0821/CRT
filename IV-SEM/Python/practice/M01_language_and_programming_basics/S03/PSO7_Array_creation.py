
'''
import array
arr = array.array('i' , [12 , 45 , 78 , 36])
print(arr , type(arr))
arr.append(40)
print(arr)
arr.append (12,45)
print(arr) 
'''
'''
arr - collection of similar data elenets that can store under a single variable.
python dosen't support arryas directly but we can use array module to create array in python.
numpy - popular library in python for numerical computations and working with arrays.(numerical python)
it can be easily access arrays and perform operations on arrays.
mainly used in ML , DS,AI Applications.
The index value starts with 0 and ends with (n-1) , 
n --> size of the arrays.
arrays can store homogeneous data elements only , lists can store hetrogeneous data elements.
'''

import numpy as np
arr = np.array([10,20,30,40])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(8))
print(np.ones(5))
print("Even numbers list is:",np.arange(2,10,2))# 2, 10,2 --> start , end , step
print("Odd numbers list is:",np.arange(1,10,2)) # 1, 10,2 --> start , end , step

n = int(input("Enter the size of the array:"))
ele = list(map(int, input("Enter the elements of the array:").split()))
print("array elements are:",np.array(ele))




