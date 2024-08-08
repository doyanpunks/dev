"""Exercises 11-1, and 11-2"""

def city(city_name, country_name, population=0):
    if population == 0:
        full_name = f"{city_name}, {country_name}"
        return full_name.title()
    else:
        full_name = f"{city_name.title()}, {country_name.title()} - population = {population}"
        return full_name