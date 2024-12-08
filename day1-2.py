import numpy as np

def similarity(array1, array2):
    total = 0
    for i in range(len(array1)):
        count = len([x for x in array2 if x == array1[i]])
        total += count*array1[i]
    return total


array1 = []
array2 = []
with open("day1.input") as file:
    for line in file:
        array1.append(int(line.split("   ")[0]))
        array2.append(int(line.split("   ")[1]))
arr1 = np.array(array1)
arr2 = np.array(array2)

similarity = similarity(arr1, arr2)
print(similarity)

