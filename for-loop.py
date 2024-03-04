for i in range(1,11):
    #print(i)
    #print("-->" + str(i))
    print(f"--> {i}")
else:
    print('END'.center(30,'~'))

cities = ['Mysore', 'Nashik', 'Surat', 'Bikaner', 'Ludhiana']

for city in cities[2:]:
    print(f"City is --> {city}")

capitals = {
    "Uttarkhand":"Dehradun",
    "Chattisgarh": "Raipur",
    "Assam" : "Dispur",
    "Arunachal Pradesh" : "Itanagar"
}

for var in capitals:
    print(f"The capital of {var} is {capitals[var]}")
else:
    print('END'.center(30,'~'))

for state,capital in capitals.items():
    print(f"--> {state} == {capital}")    

for idx,city in enumerate(cities):
    print(f" Pos : {idx}, City : {city}")