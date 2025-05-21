import numpy as np

''' Create an array with 1 dimension'''
arr1 = np.array([1, 2, 3, 4, 5])   
# print(arr1, '\n')

''' Create an array with 2 dimensions'''
arr2 = np.array([[1, 2, 3], [4, 5, 6]])   
# print(arr2, '\n')
'''Slicing & Indexing of a 2 dimension array'''
# print(arr2[0, 1])   # 1st row 2nd coloum element of array
# print(arr2[0:2, 1:3])  # Extracts first 2 rows and last 2 columns (0:2 means 0 and 1 row, 1:3 means 1 and 2 column)

''' Create an array with 3 dimensions'''
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])   
# print(arr3, '\n')

'''Specify the number of dimensions'''
arr4 = np.array([1, 2, 3, 4], ndmin=2)  
# print(arr4, '\n')

''' Change the value of an element in the array'''
arr4 [0, 1] = 10    
# print(arr4, '\n')

''' Create an array filled with zeros & specify the data type'''
arr5 = np.zeros((2, 3) ,dtype=int)   
# print('\nZero Array\n', arr5)

''' Create an array filled with ones & specify the data type'''
arr6 = np.ones((2, 3), dtype=int)   
# print('\nOne Array\n', arr6)

''' Create an array filled with a constant value of fill_value'''
arr7 = np.full((2, 3), fill_value=8)   
# print('\nfilled array\n', arr7)

''' Create an identity matrix'''
arr8 = np.eye(3, dtype=int)   
# print('\nidentity matrix\n', arr8)

''' Create an array with 5 values evenly spaced between 1 and 10'''
arr8 = np.linspace(1, 10, 4)   
# print('\nNP.linspace\n', arr8)

'''  Create an array with values from 1 to 10, with a step of 2'''
arr9 = np.arange(1, 10, 2)   
# print('\nNP.arange\n', arr9)

''' Create an array with random values'''
arr10 = np.random.randint(1, 10, size=(2, 3))   
# print('\nNP.random.randint\n', arr10)
# print('\nArray Size ----->', arr10.size)   # Get the number of elements in an array 

''' Reshape an array'''
arr10 = arr10.reshape(3, 2)   
# print('\nReshaped Array ----->\n', arr10)

'''' print the array by for loop'''
arr11 = np.array([[1, 2, 3], [4, 5, 6]])
# for i in np.nditer(arr11):   
#     print(i)
# for i in np.ndenumerate(arr11):     # print the array along with the index for loop
    # print(i)

''' Create an array with random values'''
arr12 = np.array([1,2,3,4,5])
# print('\nOriginal Array ----->\n', arr12)
arr12_copy = arr12.copy()        # Don't change the main data
arr12_copy[0] = 10
# print('\narr12.copy ----->\n', arr12, '\nDidn"t change the main data.............')
arr12_copy2 = arr12.view()        # changes the data along with the main data
arr12_copy2[0] = 20
# print('\narr12.view ----->\n', arr12, '\nChange the main data................')

''' Concatenate of two arrays'''
arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[5, 6], [7, 8]])
# print('\nConcatenated array -----> \n', np.concatenate((arr_1, arr_2), axis=0),'\n')
# print('\nConcatenated array -----> \n', np.concatenate((arr_1, arr_2), axis=1),'\n')
# print(np.hstack((arr_1,arr_2)),'\n')    # concatenate according axis=1 or Y-axis
# print(np.vstack((arr_1,arr_2)),'\n')    # concatenate according axis=0 or X-axis
# print(np.dstack((arr_1,arr_2)),'\n')    # concatenate according axis=2 or Z-axis

''' Find Element Index in the array(Boolean Masking)'''
arr_3 = np.array(([0,3,4,1,2],[0,8,9,6,7]))
# print(np.where(arr_3 == 0))     # finding the index of an element  "output: (array([0, 1]), array([0, 0]))" means [0,0] and [1,0]
# print(np.where(arr_3 > 5))      # element greater than 5   "output: (array([1, 1, 1, 1]), array([1, 2, 3, 4]))" means [1, 1], [1,2], [1,3] and [1,4]    

''' Finding values Count and 1st index of the array'''
arr_4 = np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 8, 2])
# print(np.unique(arr_4, return_index=True, return_counts=True))      # Output: (array([,,1,,]), (array([,,2,,]), (array([,,3,,]))  1 -> values, 2 -> index, 3 -> value.count

''' Inserting an element in the array'''
arr_5 = np.insert(arr_4, (5), 10)  # insert 10 at index 5 
# print(arr_5)

'''Sorting of the array'''
arr_6 = np.array(([0,3,4,1,2],[0,8,9,6,7]))
# print('\nSorted Array ----->\n', np.sort(arr_6)) 

'''Creation of Matrix and Arrithmatic opration( +, * )'''
matrix1 = np.matrix('1 2; 3 4')
matrix2 = np.matrix('5 6; 7 8')
# print(f'Matrix1 -->\n {matrix1}\n\nMatrix2 -->\n {matrix2}\n\n')
# print(matrix1 * matrix2)   # Multiplication two matrices

'''if you slice a array it will return a view of the original array means it will change the original array'''
arr_7 = np.array([1, 2, 3, 4, 5])
a = arr_7[2:4]  # slicing the array
# print(a)
a[0] = 10
# print(arr_7)  # original array will also change


'''Finding the mean, median, standard deviation and variance of the array'''
arr_8 = np.array(([2, 5, 8, 3], [10, 18, 12, 15]))
# print(np.mean(arr_8))                 # finding the mean of the array
# print(np.median(arr_8))               # finding the median of the array
# print(np.std(arr_8))                  # finding the standard deviation of the array
# print(np.var(arr_8))                  # finding the variance of the array

'''Function and Methods of the array'''
print(np.min(arr_8))            # finding the minimum value of the array 
print(np.max(arr_8))            # finding the maximum value of the array
print(np.sum(arr_8))            # finding the sum of the array
print(np.prod(arr_8))           # finding the product of the array
print(np.cumsum(arr_8))         # finding the cumulative sum of the array
print(np.percentile(arr_8, 50)) # finding the 50th percentile of the array
print(np.diff(arr_8))           # finding the difference of the array
print(np.argmax(arr_8))         # finding the index of the maximum value of the array
print(np.argmin(arr_8))         # finding the index of the minimum value of the array
print(np.unique(arr_8))         # finding the unique values of the array

