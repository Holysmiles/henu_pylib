import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

arr1 = array[1:3, 0:2]
print(arr1)

arr2 = array[:, 1:2]
print(arr2)

arr3 = array[1:2, 2:]
print(arr3)

arr4 = array[1:2, :]
print(arr4)

new_array = array * 2
row_max = np.max(new_array, axis=1)
col_max = np.max(new_array, axis=0)
print("按行最大值：", row_max)
print("按列最大值：", col_max)
