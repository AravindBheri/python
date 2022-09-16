import array

arr = array('i', [])

n = int(input("Enter the size of the array: "))

for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)

for el in arr:
    print(el)

val = int(input("Enter the element you want to find:"))

# indexx = 0

# for e in arr:
#     if e == val:
#         print("Index is " + str(indexx))
#         break
#     indexx += 1

print("Index is " + str(arr.index(val)))

