from city_functions import city

def test_city_country():
    city_name = city('santiago', 'chile')
    assert city_name == 'Santiago, Chile'

def test_city_country_population():
    city_name = city('santiago', 'chile', 500000)
    assert city_name == 'Santiago, Chile - population = 500000'