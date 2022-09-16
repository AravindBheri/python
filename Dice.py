import random
import sys

def roll():
  a = random.randint(1,6)
  return a
  
def doubleroll():
  b = random.randint(1,6)
  c = random.randint(1,6)
  return b+c
  
flag = 1
while(flag):
  print("1.Start")
  print("2.Exit")
  option = int(input())
  if(option == 1 or option == 2):
    if(option == 1):
      print("3.Roll")
      print("4.Double Roll")
      choice = int(input())
      if(choice == 3):
        print("Single roll : " + str(roll()))
      if(choice == 4):
        print("Double roll : " + str(doubleroll()))
    if(option == 2):
      sys.exit("Done!")
        

  
      

