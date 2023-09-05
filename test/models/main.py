from src.models.restaurant import Restaurant
from src.models.ice_cream_stand import IceCreamStand

# RESTAURANT TEST

'''
my_restaurant = Restaurant("Meu Restaurante", "Comida Italiana")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(50)
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served(10)
my_restaurant.describe_restaurant()
my_restaurant.close_restaurant()
'''

# ICE CREAM STAND TEST
'''
my_icecreamstand = IceCreamStand("Kibon", "Sorvetes", ["Chocolate", "Morango", "Creme"])
my_icecreamstand.flavors_available()
my_icecreamstand.find_flavor("Flocos")
my_icecreamstand.find_flavor("Morango")
my_icecreamstand.add_flavor("Uva")
my_icecreamstand.flavors_available()

my_icecreamstand = IceCreamStand("Kibon", "Sorvetes", [''])
my_icecreamstand.flavors_available()
my_icecreamstand.find_flavor("Flocos")
my_icecreamstand.add_flavor("Uva")
my_icecreamstand.flavors_available()
'''
