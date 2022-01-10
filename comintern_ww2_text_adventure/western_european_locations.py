class WestEurope:
    def __init__(self, north, north_east, east, south_east, south, south_west, west, north_west):
        self.north = north
        self.north_east = north_east
        self.east = east
        self.south_east = south_east
        self.south = south
        self.south_west = south_west
        self.west = west
        self.north_west = north_west
        self.description = None

def western_cities():
    west_cities = []

    london = WestEurope(None, None, None, None, None, None, None, None)
    london.description = ("london")
    west_cities.append(london)

    paris = WestEurope(None, None, None, None, None, None, None, None)
    paris.description = ("paris")
    west_cities.append(paris)
