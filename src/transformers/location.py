import re


def get_departement(location_array):
    departements = []
    for location in location_array:
        try:
            departements.append(int(location[location.find("(") + 1:location.find(")")]))
        except ValueError:
            departements.append(0)
    return departements


def get_city(location_array):
    cities = []
    regex = r"(.*?)\s*\("
    # .*(?<!\))$|([\w ]*)\(
    for location in location_array:
        if "(" in location:
            city = re.findall(regex, location)
            cities.append(city[0])
        elif location[0].isdigit():
            city = location.split()[1]
            cities.append(city)
        else:
            cities.append(location)
    return cities
