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
    vdladivostok = Pacific(1, None, None, None, None, 2, None, None)
    vdladivostok.description = ("Zhukov you have been assigned to the pacific theatre.\n"
                                "you are currently in Vdladivostok. your objective...make it to Tokyo Japan before\n"
                                "the capitalists. Go north to Khabarovsk or south west to Pyongyang.")
    pacific.append(vdladivostok)

    khabarovsk = Pacific(None, None, None, None, 0, None, None, None)
    khabarovsk.description = ("Moscow knows very little about their siberian city of Khabarovsk.\n"
                              "Go south to Vdladivostok.")
    pacific.append(khabarovsk)

    pyongyang = Pacific(None, 0, None, None, 3, None, None, None)
    pyongyang.description = ("Pyongyang. Soon to be the capital of the DPRK. We must capture this city to ensure\n"
                             "we keep them as an ally. Move south to Seoul or north east to Vdladivostok")
    pacific.append(pyongyang)

    seoul = Pacific(None, None, None, 4, None, None, None, 2)
    seoul.description = ("Seoul. What a lovely center of korean culture this city contains.\n"
                         "Would be a shame if someone...liberated it. Oh wait...the Japanese already did.\n"
                         "Move south east to pusan or north west to Pyongyang.")
    pacific.append(seoul)

    pusan = Pacific(None, None, None, 5, None, None, None, 3)
    pusan.description = ("Pusan. This city was bombed to the ground by the Japanese. \n"
                         "Go south east to nagasaki or north west to Seoul.")
    pacific.append(pusan)

    nagasaki = Pacific(None, 7, None, None, None, None, None, 4)
    nagasaki.description = ("Nagasaki Japan. We selected this city as the beginning of our invasion of the Japanese homeland.\n"
                            "However we are experiencing fierce resistance. Perhaps an alternate tactic should be used to win.\n"
                            "Go north east to Hiroshima or north west to Pusan")
    pacific.append(nagasaki)

    hiroshima = Pacific(None, 8, None, None, None, 5, None, None)
    hiroshima.description = ("Hiroshima Japan. We are experiencing far more resistance than we did in Nagasaki\n"
                             "We should use one of our nuclear weapons to end this city.\n"
                             "Go north east to Osaka or go south west to Nagasaki.")
    pacific.append(hiroshima)

    osaka = Pacific(None, 9, None, None, None, 6, None, None)
    osaka.description = ("Osaka Japan. Go north east to Tokyo or south west to Hiroshima.")
    pacific.append(osaka)

    tokyo = Pacific(None, 10, None, None, None, 7, None, None)
    tokyo.description = ("Tokyo Japan. Go south west to Osaka or north east to Saporo")
    pacific.append(tokyo)

    saporo = Pacific(None, None, None, None, 10, None, 0, None)
    saporo.description = ("Saporo Japan. Go south to Saporo or west to Vdladivostok.")
    pacific.append(saporo)

    sendai = Pacific(9, None, None, None, 8, None, None, None)
    sendai.description = ("Sendai Japan. Go south to Tokyo or north to Saporo.")
    pacific.append(sendai)

    return pacific