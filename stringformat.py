animal = "cow"
item = "moon"

# print("The {} jumped over the {}".format("cow", "moon"))
# print("The {} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {1}".format(animal, item)) #positional args
# print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon")) #keyword args

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

first_name = "bro"
last_name = "code"


# print("Hello, my name is {:10}. Nice to meet you :)".format(name))
# print("Hello, my name is {0:10} {1:10}. Nice to meet you :)".format(first_name, last_name))
# print("Hello, my name is {first_name:10} {last_name:10}. Nice to meet you :)".format(first_name = "bro", last_name = "code"))
# print("Hello, my name is {:<10}. Nice to meet you :)".format(first_name)) #left align
# print("Hello, my name is {:>10}. Nice to meet you :)".format(first_name))   #right align
# print("Hello, my name is {:^10}. Nice to meet you :)".format(first_name)) #centre align

number = 1000

# print("The number of pi is {:.2f}".format(number)) #to display two places after decimal
# print("The number is {:,}".format(number)) #adds comma after thousands
# print("The number is {:b}".format(number)) #to display the number in binary format
# print("The number is {:o}".format(number))  #octal form of number
# print("The number is {:X}".format(number)) #x for lowercase and X for uppercase
print("The number is {:e}".format(number)) #e for lowcase and E for Upcase