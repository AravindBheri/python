name = ["Andy", "Aravind", "Bhanu", "Vinay", "Aman"]
time = [1, 3, 4, 2, 5]
total = []

for i in range(len(name)):
    total.append([time[i], name[i]])
    
total.sort()

for t in total:
    print(t)

# for i in range(len(total)):
#     print(total[i][1], end = ' ')



