import text_adventure_files
import adolf_sprite_ai
import arcade
SPRITE_SCALING = 0.5

class Europa:
    def __init__(self, north, north_east, east, south_east, south, south_west, west, north_west):
        """Creation of variables that will be constraints upon sprite movement"""
        self.north = north
        self.north_east = north_east
        self.east = east
        self.south_east = south_east
        self.south = south
        self.south_west = south_west
        self.west = west
        self.north_west = north_west
        self.background = None
        self.germans = None

def city_one():
    moscow = Europa(None, None, None, None, None, None, None, None)
    moscow.germans = arcade.SpriteList()

    return moscow

def city_two():
    stalingrad = Europa(None, None, None, None, None, None, None, None)
    stalingrad.germans = arcade.SpriteList()

    return stalingrad

def city_three():
    kiev = Europa(None, None, None, None, None, None, None, None)
    kiev.germans = arcade.SpriteList()

    return kiev

def city_four():
    leningrad = Europa(None, None, None, None, None, None, None, None)
    leningrad.germans = arcade.SpriteList()

    return leningrad

def city_five():
    brest_litvosk = Europa(None, None, None, None, None, None, None, None)
    brest_litvosk.germans = arcade.SpriteList()

    return brest_litvosk

def city_six():
    riga = Europa(None, None, None, None, None, None, None, None)
    riga.germans = arcade.SpriteList()

    return riga

def city_seven():
    warsaw = Europa(None, None, None, None, None, None, None, None)
    warsaw.germans = arcade.SpriteList()

    return warsaw

def city_eight():
    konigsberg = Europa(None, None, None, None, None, None, None, None)
    konigsberg.germans = arcade.SpriteList()

    return konigsberg

def city_nine():
    kursk = Europa(None, None, None, None, None, None, None, None)
    kursk.germans = arcade.SpriteList()

    return kursk

def city_ten():
    breslau = Europa(None, None, None, None, None, None, None, None)
    breslau.germans = arcade.SpriteList()

    return breslau

def city_eleven():
    bucharest = Europa(None, None, None, None, None, None, None, None)
    bucharest.germans = arcade.SpriteList()

    return bucharest

def city_twelve():
    budapest = Europa(None, None, None, None, None, None, None, None)
    budapest.germans = arcade.SpriteList()

    return budapest

def city_thirteen():
    prague = Europa(None, None, None, None, None, None, None, None)
    prague.germans = arcade.SpriteList()

    return prague

def city_fourteen():
    stettin = Europa(None, None, None, None, None, None, None, None)
    stettin.germans = arcade.SpriteList()

    return stettin

def city_fifteen():
    berlin = Europa(None, None, None, None, None, None, None, None)
    berlin.germans = arcade.SpriteList()

    return berlin