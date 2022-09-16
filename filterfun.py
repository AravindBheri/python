friends = [("Amresh", 21),
            ("Aravind", 21),
            ("Bhanu", 22),
            ("Vinay", 21),
            ("Andy", 16),
            ("Rod", 17)]

age = lambda data:data[1] >= 18

party_friends = list(filter(age, friends))

for i in party_friends:
    print(i)