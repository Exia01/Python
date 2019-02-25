# Importing everything in both modules:

# import bananas
import apples

print(apples.offer())

offer = apples.offer()
print(offer)

# print(bananas.dip_in_chocolate())


# Importing a single function from bananas:
from bananas import dip_in_chocolate as dip
print(dip())
