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
    regex = re.compile("(.*?)\s*\(")
    for location in location_array:
        cities.append(re.findall(regex, location))
    return cities