import os

from numpy import source

source = 'C:\\Users\\Aravind\\OneDrive\\Desktop\\python\\FileHandling\\text.txt'
destination = 'C:\\Users\\Aravind\\Desktop\\text.txt'

try:
    if os.path.exists(source):
        print(source + " is already there!! :(")  
    else:
        os.replace(source, destination)
        print("File is moved!! :)")
except FileNotFoundError:
    print(source + " was not found")