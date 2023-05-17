# defines the data scructure, a list containing different dictionaries for each item (countries visited)
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# function responsible for getting user input, processing it and appending it to travel log list.
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


# testing function
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log[0])
print(travel_log[1])
print(travel_log[2])

