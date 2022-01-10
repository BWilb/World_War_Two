class Europe:
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

def cities():
    europe_cities = []
    """Russian Cities"""
    moscow = Europe(None, None, None, None, None, 1, None, 3)
    moscow.description = ("\nZhukov, since you have been assigned to the European front...your first objective will be to\n"
                          "protect our glorious capital. Moscow has destroyed in flames before, don't hesitate to raze it all,\n"
                          "so that the invaders will have NOTHING!!! Go south west to Stalingrad, north west to Leningrad,\n"
                          "or west to Riga")
    europe_cities.append(moscow)

    stalingrad = Europe(None, None, None, None, None, None, 2, 0)
    stalingrad.description = ("\nStalingrad. If you let this city fall to enemy hands YOU WILL BE TRIED AND\n"
                              "CHARGED WITH CAPITAL PUNISHMENT; FOR THIS CITY BEARS THE NAME OF STALIN!!\n"
                              "Go north west to Moscow or west to Kiev")
    europe_cities.append(stalingrad)

    kiev = Europe(None, 0, 1, None, None, None, None, None)
    kiev.description = ("\nThe famous city of the Cossacks...meh. Go north east to Moscow or east to Stalingrad.")
    europe_cities.append(kiev)

    leningrad = Europe(None, None, None, 0, None, None, None, None)
    leningrad.description = ("\nIf you let one german soldier inside Leningrad, you will be hanged.\n"
                             "Go south east to Moscow or south west to Riga.")
    europe_cities.append(leningrad)
    """Going to finish the rest later"""

    return europe_cities