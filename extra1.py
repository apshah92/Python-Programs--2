from itertools import product

for items in product('abcd',repeat=3):
    print ''.join(items)
