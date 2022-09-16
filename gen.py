def topten():

    n = 1

    while n <= 10:
        sqr = n*n
        yield sqr
        n += 1

values = topten()

for val in values:
    print(val)