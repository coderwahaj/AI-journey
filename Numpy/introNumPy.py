import numpy as np

arr = np.array([10, 20, 30,40,50,60])
arr1=np.arange(1,25)
print(arr)  # Output: [1 2 3]
## Indexing 
print('Indexing : ')
print(arr[3])
print(arr[-5])

print ('---------------------------------')
##Slicing 

print('Slicing : ')
print(arr[4:0:-2])

print ('---------------------------------')
## Fancy Indexing

print('Fancy Indexing(Print multiple elements in one go ) : ')
print(arr[[0,3,5]])

print ('---------------------------------')
## Boolean Masking 

print('Boolean Masking (Filtering on condition) : ')
print((arr > 40) & (arr < 60))

print(arr[(arr>40)& (arr<60)] )

print ('---------------------------------')
## Reshaping 

print('Reshaping : ')
print(arr1.reshape(2,4,3))
print ('---------------------------------')
# If we don’t want to calculate one dimension manually.
#This works if only one dimension is -1
#Affect the original array just return the View

print('Reshaping with one dimension unknown set to -1 : ')
result = arr1.reshape(2,-1,3)
print(arr1.reshape(2,-1,3))

print ('---------------------------------')
# Flatten the result 3d array into 1D array
#ravel return the view and flatten returns the copy

print ('With Ravel return view ')
print (result.ravel())
print ('---------------------------------')
print ('With Flatten return copy ')
print (result.flatten())
print ('---------------------------------')
print(result)

