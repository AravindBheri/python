pos = 0

def search(list, n):
    i = 0
    
    # while i < len(list):
    #     if list[i] == n:
    #         globals()['pos'] = i
    #         return True
    #     i = i + 1
    # return False
    
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
        
list = [1,2,3,4,5,6]

if search(list, 3):
    print("Element found at: " + str(pos + 1))
else:
    print("Element not found!!")
