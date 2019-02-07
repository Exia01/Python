# This code picks a random food item:
from random import choice
food = choice(["cheese pizza", "quiche", "morning bun",
               "gummy bear", "tea cake"])  # DON'T CHANGE!


bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
stock = bakery_stock.get(food)
class Error(Exception):
    pass

class NotInStock(Error):
    """When not in stock this will pass error"""
    pass
class NotFound(Error):
    """When not in bakery_stock"""
    pass

try:
    if stock:
        # item = bakery_stock.get(food)
        if stock > 0:
            print(f'{stock} left')
        else:
            raise NotFound
    else:
        raise NotFound
except NotFound:
    print('We don\'t make that')



# Simpler way_1
quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")

# Simpler way_2
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")