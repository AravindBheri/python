pos = 0

def search(list, n):
    
    lb = 0
    ub = len(list) - 1
    
    while lb <= ub:
        mid = (lb + ub) // 2
        
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lb = mid + 1
            else:
                ub = mid - 1
    return False


list = [1,2,3,4,5,6,7,8]
list.sort()


if search(list, 2):
    print("Element found at: " + str(pos + 1))
else:
    print("Element not found!!")