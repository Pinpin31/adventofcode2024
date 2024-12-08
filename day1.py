import numpy as np
array1 = []
array2 = []
with open("day1.input") as file:
    for line in file:
        array1.append(int(line.split("   ")[0]))
        array2.append(int(line.split("   ")[1]))
array1.sort()
array2.sort()
arr1 = np.array(array1)
arr2 = np.array(array2)

distance = np.sum(np.abs(arr1 - arr2))
print(distance)

