import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'storefront.settings')

import django
django.setup()

from products.models import (Type, Colour)

colours = {'red': 0.20, 'blue': 0.20, 'green': 0.40, 'yellow': 0.50, 'pink': 0.60, 'purple': 0.60, 'orange': 0.70,
           'white': 0.40, 'maroon': 0.40, 'lilac': 0.60, 'peach': 0.80, 'jade': 0.80, 'gold': 1.20, 'turquoise': 1.00,
           'teal': 0.90, 'rainbow': 1.50}

types = {'rose': 1.00, 'tulip': 1.50, 'daisy': 1.30, 'poppy': 1.30, 'sunflower': 1.60, 'carnation': 1.00, 'lily': 1.30,
         'dahlia': 1.50, 'peony': 1.20, 'marigold': 1.00, 'foxglove': 1.10, 'iris': 1.30, 'forget-me-nott': 1.40,
         'violet': 1.30 , 'aster': 1.30, 'crocus': 1.50}

def create_types(types):
    for x in types:
        nm = x
        pr = types.get(x)
        t = Type.objects.get_or_create(name=nm,price=pr)[0]
        t.save()

def create_colours(colours):
    for x in colours:
        nm = x
        pr = colours.get(x)
        c = Colour.objects.get_or_create(name=nm,price=pr)[0]
        c.save()


if __name__ == '__main__':
    print("Creating flower attributes..")
    create_types(types)
    create_colours(colours)
    print("Flower attributes created!")
