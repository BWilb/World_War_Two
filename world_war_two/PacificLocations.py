class Pacific:
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

def locations():
    pacific = []
    vdladivostok = Pacific(1, None, None, None, None, None, None, None)
    vdladivostok.description = ("Zhukov you have been assigned to the pacific theatre.\n"
                                "you are currently in Vdladivostok. your objective...make it to Tokyo Japan before\n"
                                "the capitalists. Go north to Khabarovsk.")
    pacific.append(vdladivostok)

    khabarovsk = Pacific(None, None, None, None, 0, None, None, None)
    khabarovsk.description = ("Moscow knows very little about their siberian city of Khabarovsk.\n"
                              "Go south to Vdladivostok.")
    pacific.append(khabarovsk)

    return pacific