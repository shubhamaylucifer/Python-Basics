my_function = lambda x: x ** 2

print(f" Square of 5 is {my_function(5)}")
print(f" Square of 10 is {my_function(10)}")

cities = ['Lucknow', 'Gorakhpur', 'Gaya', 'Dhanbad', 'Siliguri', 'Jorhat', 'Imphal']

data = []
for city in cities:
    if(city.startswith('G')):
        data.append(city)

print(f"Data : {data}")

data = list(filter(lambda x: x.startswith('G'), cities))

print(data)


print("--" * 30)

updated_cities = []
for city in cities:
    updated_cities.append(
        'City --> ' + city
    )

print(f"updated_cities: {updated_cities}")

updated_cities = list(
    map(lambda x: 'City ->' + x, cities)
)

print(f"updated_cities using lambda: {updated_cities}")
