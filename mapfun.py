store = [("Shirt", 20.0), 
         ("Pants", 25.0),
         ("Socks", 5.0),
         ("Shoes", 10.0)]

to_inr = lambda data: (data[0], data[1] * 78) 
new_store = list(map(to_inr, store))
for i in new_store:
    print(i)