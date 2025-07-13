# np.isnan(array)

import numpy as np
print ('Handling Missing Values')

arr= np.array([1,2,np.nan,4,5,np.nan,7,8,9,10])

print(np.isnan(arr))
print ('---------------------------------')


print(np.nan_to_num(arr, nan=10))
print ('---------------------------------')


arr= np.array([1,2,3,4,5,6,7,np.inf,9,-np.inf])

print(np.isinf(arr))
print(np.nan_to_num(arr,posinf=1000,neginf=-1000))
print ('---------------------------------')
