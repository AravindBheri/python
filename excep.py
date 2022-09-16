a = 10
b = 5

try:
    print("Resource opened!!")
    print(a/b)
    num = int(input("enter a number:"))
    print(num)

except ZeroDivisionError:
    print("You can't divide a number by zero!! :(")

except ValueError:
    print("Invalid input!! :(")

except Exception as e:
    print("Somthing went wrong! :(")

finally:
    print("Resource Closed!! :)")