# BroadCasting
import numpy as np
print('Calculate Discount for all elements (without using for loop)  : ')
prices = np.array([10, 20, 30,40,50,60])
discount = 10
discounted_prices=prices-((prices*10)/100)
print(prices)
print(discounted_prices)  

print ('---------------------------------')


#Expanding Single Element
print('Arithematic Operations on expanding single element  of array  : ')
arr = np.array([10, 20, 30,40,50,60])
value = 10
add=arr+value

multiply=arr*value
print('Add single element 10 with all the array elements')
print(add)
print('Multiply single element 10 with all the array elements')
print(multiply)  

print ('---------------------------------')

#Matching Dimensions
print('Arithematic Operations on matching dimension of array  : ')
arr1 = np.array([10, 20, 30,40,50,60])
arr2 = np.array([10, 20, 30,40,50,60])
add=arr1+arr2

multiply=arr1*arr2
print('Add two arrays elements')
print(add)
print('Multiply two arrays elements')
print(multiply)  

print ('---------------------------------')

#Incomaptible Dimensions
# print('Arithematic Operations on Incomaptible dimension of array  : ')
# arr1 = np.array([[10, 20, 30],[40,50,60]])
# arr2 = np.array([10, 20, 30,40,50,60])
# #arr2 = np.array([10, 20, 30,40,50,60]).reshape(2,1,3)
# add=arr1+arr2

# multiply=arr1*arr2
# try:
#     print('Add two arrays elements')
#     print(add)
#     print('Multiply two arrays elements')
#     print(multiply)
# except ValueError as e:
#     print(f"Error: {e}")

# print ('---------------------------------')

#1d to 2d
print('Arithematic Operations on 1d to 2d dimension of array  : ')
arr1 = np.array([[10, 20, 30],[40,50,60]])
arr2 = np.array([10, 20, 30])
add=arr1+arr2

multiply=arr1*arr2
try:
    print('Add two arrays elements')
    print(add)
    print('Multiply two arrays elements')
    print(multiply)
except ValueError as e:
    print(f"Error: {e}")

print ('---------------------------------')
