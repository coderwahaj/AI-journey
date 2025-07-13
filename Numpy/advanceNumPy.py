# np.insert(array,index,value,axis=None)
#array - Original Array 
#index - Position where to place 
#Value - Original Value to be place
#axis  - None (1d Array in case)
# axis = 0 ,row-wise
# axis = 1 ,column-wise 

#Insert an element in 1d array 
import numpy as np
print('Insert an element in 1d array  : ')
arr = np.array([10, 20, 30,40,50,60])
new_arr=np.insert(arr,2,25,None)
print(new_arr)
print(arr)  

print ('---------------------------------')

new_arr=np.insert(arr,2,[25,26],None)
print(new_arr)
print(arr)  

print ('---------------------------------')

#Insert an element in 2d array 
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
print ('Insert an element in 2d array :')
new_arr_2d=np.insert(arr_2d,3,[7,8],axis=1)
print(new_arr_2d)
print(arr_2d)  

print ('---------------------------------')

#Append an element in 1d array 

print ('Append an element in 1d array :')
append_arr=np.append(arr,[70,80])
print(append_arr)
print(arr)  

print ('---------------------------------')


array = np.array([[1, 2], [3, 4]])
row = np.array([[5, 6]])
col=np.array([[5],[6]])
#Append an element in 2d array 

# Append row-wise (add a new row)
print ('Append an element in 2d array in row-wise :')

result1 = np.append(array, row, axis=0)
print(result1)
# Append col-wise (add a new col)

print ('Append an element in 2d array in col-wise :')
result2 = np.append(array, col, axis=1)
print(result2)


print ('---------------------------------')
#Append an element in 3d array 

print ('Append an element in 3d array:')

a = np.arange(12).reshape(2, 2, 3)
print(a)
b = np.arange(12, 24).reshape(2, 2, 3)
print(b)

# Shape: (2, 2, 3) + (2, 2, 3) → valid
print ('After Append  in 3d array  :')

c = np.append(a, b, axis=0)
print(c)
print(c.shape)  # (4, 2, 3)

print ('---------------------------------')


#Concat two arrays
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print ('Concat two arrays :')
concat_arr=np.concatenate([arr1,arr2])
print(concat_arr)


print ('---------------------------------')

#Delete an element from array
#np.delete(array,index,axis=None )

print ('Delete an element from the array :')
delete_arr=np.delete(arr,2,axis=None)
print(delete_arr)


print ('---------------------------------')

#Delete an element from 2d array 

# Delete row-wise (Delete a new row)
print ('Delete an element in 2d array in row-wise :')

new_arr = np.delete(array, 0, axis=0)
print(array)
print(new_arr)
# Append col-wise (Delete a new col)

# print ('Delete an element in 2d array in col-wise :')

print ('Delete an element in 2d array in col-wise :')
new_arr = np.delete(array, 0, axis=1)
print(array)
print(new_arr)




#Stacking arrays 

#Stack row-wise vstack()
print ('Stack arrays row-wise :')

new_arr = np.vstack((arr1,arr2))
print(new_arr)

#Stack col-wise hstack()
print ('Stack arrays col-wise :')

new_arr = np.hstack((arr1,arr2))
print(new_arr)

print ('---------------------------------')

#Spliting
# 1-In equal Parts

print ('Split arrays in equal parts :')
print(arr_2d)
new_arr = np.split(arr,3)
print(new_arr)

print ('Split arrays in horizontal (col-wise):')

# 2-In col-wise 
new_arr = np.hsplit(arr_2d, 2)
print(new_arr)

print('Split arrays in vertical (row-wise) :')

# 3-In row-wise
new_arr = np.vsplit(arr_2d, 2)
print(new_arr)

print ('---------------------------------')

## Advance things 

a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
print(a[:,1:2])





#np.linspace(start, stop, num)

print(np.linspace(0, 1, 5))
# Output: [0.   0.25 0.5  0.75 1.  ]

#np.logspace(start_exp, stop_exp, num)

print(np.logspace(1, 4, 4))
# Output: [  10.  100. 1000.].
# When to use: For exponentially spaced ranges (ML models like SVM with different C values).


#np.tile(array, reps)
np.tile([1, 2], 3)
# Output: [1 2 1 2 1 2]

#np.repeat(array, repeats)
np.repeat([1, 2], 3)
# Output: [1 1 1 2 2 2]

#np.unique(arr, return_counts=True)
print(np.unique([1, 2, 2, 3], return_counts=True))
# Output: (array([1, 2, 3]), array([1, 2, 1]))

# np.sort(arr)         # returns sorted array
#np.argsort(arr)      # returns index positions of sorted elements

arr = np.array([30, 10, 20])
np.argsort(arr)  # Output: [1 2 0]
#When to use: Ranking systems, leaderboard, top-N sorting.

#np.where(condition, x, y)

arr = np.array([1, 2, 3])
np.where(arr > 1, 'yes', 'no')
# Output: ['no', 'yes', 'yes']

#np.clip(arr, min_val, max_val)
arr = np.array([1, 5, 10])
print(arr)
print(np.clip(arr, 3, 7))
# Output: [3 5 7]
# When to use: Normalization, bounding outputs, image processing.

