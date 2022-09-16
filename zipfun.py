usernames = ["Aravind", "Emrit", "Andy"]
passwords = ("!@3", "^&*", "90*")
mail = ["Google", "outlook", "Duck"]

#data = dict(zip(usernames, passwords))
#data = list(zip(usernames, passwords, mail))
data = tuple(zip(usernames, passwords, mail))
#data = zip(usernames, passwords, mail)
for d in data:
    print(d)
    
print(data)
