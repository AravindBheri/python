import array

arr1 = array('i', [10,42,3])
arr2 = array('i', [20,2,30])

max = arr1[0]

for i in arr1:
    if max < i:
        max = i
print(max)

min = arr1[0]

for i in arr1:
    if min > i:
        min = i
print(min)

