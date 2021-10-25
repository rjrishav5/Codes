#creating a 2-d array
import numpy as np
arr = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3]])
print(arr)
print(len(arr))

# Insert 
new_arr = np.insert(arr,0,[[0,0,0,0]],axis=0) 
print(new_arr)
print(len(new_arr))
'''
line 8:
arr = the 2-d array in which you have to insert
0 = position 
[[0,0,0,0]] = row/column to add
axis = 0 for row and 1 for column
'''

new1_arr = np.append(new_arr,[[0,1,2,3]],axis=0) 
print(new1_arr)


#traverse
def traversed(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=' ')


traversed(new1_arr)