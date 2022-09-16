import functools

fnums = [5,4,3,2,1]

fact = functools.reduce(lambda x, y : x * y, fnums)
print(fact)