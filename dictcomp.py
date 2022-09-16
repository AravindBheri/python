cities = {"Hyderabad" : "Sunny", "Bangalore" : "Chill", "Vizag" : "Cloudy", "kadapa" : "Sunny"}
# hot_cities = {key: value for key,value in cities.items() if value == "Sunny"}
def checkclimate(value):
    if value == "Sunny":
        return "Warm!!"
    if value == "Chill" or value == "Cloudy":
        return "Cold"
# hot_cities = {key : ("Warm" if value == "Sunny" else "Cold") for key,value in cities.items()}
hot_cities = {key: checkclimate(value) for key,value in cities.items()}
print(hot_cities)