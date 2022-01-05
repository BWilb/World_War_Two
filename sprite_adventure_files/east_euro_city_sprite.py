import random

import text_adventure_files.adolf_hitler
import adolf_sprite_ai
import arcade
SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1500

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
        self.floor_list = arcade.SpriteList()

def city_one():
    """City of Moscow"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    moscow = Europa(None, None, None, None, None, None, None, None)
    moscow.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        moscow.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        moscow.floor.center_x = x
        moscow.floor.center_y = 216
        moscow.floor_list.append(moscow.floor)
    for i in range(len(adolf.troop_list) // 45):
        moscow.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            moscow.german.center_x = random.randrange(SCREEN_WIDTH)
            moscow.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(moscow.german, moscow.floor_list)
            german_german = arcade.check_for_collision_with_list(moscow.german, moscow.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True

        moscow.germans.append(moscow.german)

    moscow.background = arcade.load_texture("moscow.jpg")
    return moscow

def city_two():
    """City of Stalingrad/Volograd"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    stalingrad = Europa(None, None, None, None, None, None, None, None)
    stalingrad.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        stalingrad.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        stalingrad.floor.center_x = x
        stalingrad.floor.center_y = 216
        stalingrad.floor_list.append(stalingrad.floor)

    for i in range(len(adolf.troop_list) // 45):
        stalingrad.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            stalingrad.german.center_x = random.randrange(SCREEN_WIDTH)
            stalingrad.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(stalingrad.german, stalingrad.floor_list)
            german_german = arcade.check_for_collision_with_list(stalingrad.german, stalingrad.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        stalingrad.germans.append(stalingrad.german)
    stalingrad.background = arcade.load_texture("volograd.png")

    return stalingrad

def city_three():
    """City of Kiev"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    kiev = Europa(None, None, None, None, None, None, None, None)
    kiev.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        kiev.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        kiev.floor.center_x = x
        kiev.floor.center_y = 216
        kiev.floor_list.append(kiev.floor)

    for i in range(len(adolf.troop_list) // 45):
        kiev.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            kiev.german.center_x = random.randrange(SCREEN_WIDTH)
            kiev.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(kiev.german, kiev.floor_list)
            german_german = arcade.check_for_collision_with_list(kiev.german, kiev.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        kiev.germans.append(kiev.german)

        kiev.background = arcade.load_texture("kiev.jpg")

    return kiev

def city_four():
    """City of leningrad"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    leningrad = Europa(None, None, None, None, None, None, None, None)
    leningrad.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        leningrad.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        leningrad.floor.center_x = x
        leningrad.floor.center_y = 216
        leningrad.floor_list.append(leningrad.floor)

    for i in range(len(adolf.troop_list) // 45):
        leningrad.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            leningrad.german.center_x = random.randrange(SCREEN_WIDTH)
            leningrad.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(leningrad.german, leningrad.floor_list)
            german_german = arcade.check_for_collision_with_list(leningrad.german, leningrad.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        leningrad.germans.append(leningrad.german)

        leningrad.background = arcade.load_texture("leningrad.jpg")

    return leningrad

def city_five():
    """Place of Brest-Litvosk"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    new_adolf = adolf_sprite_ai.AdolfHitler("robot_idle.png", SPRITE_SCALING)
    brest_litvosk = Europa(None, None, None, None, None, None, None, None)
    brest_litvosk.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        brest_litvosk.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        brest_litvosk.floor.center_x = x
        brest_litvosk.floor.center_y = 216
        brest_litvosk.floor_list.append(brest_litvosk.floor)

    for i in range(len(adolf.troop_list) // 45):
        brest_litvosk.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            brest_litvosk.german.center_x = random.randrange(SCREEN_WIDTH)
            brest_litvosk.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(brest_litvosk.german, brest_litvosk.floor_list)
            german_german = arcade.check_for_collision_with_list(brest_litvosk.german, brest_litvosk.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
            new_adolf.german_list.append(brest_litvosk.german)
        brest_litvosk.germans.append(brest_litvosk.german)

        brest_litvosk.background = arcade.load_texture("brest-litvosk.jpg")

    return brest_litvosk

def city_six():
    """City of Riga"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    riga = Europa(None, None, None, None, None, None, None, None)
    riga.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        riga.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        riga.floor.center_x = x
        riga.floor.center_y = 216
        riga.floor_list.append(riga.floor)

    for i in range(len(adolf.troop_list) // 45):
        riga.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            riga.german.center_x = random.randrange(SCREEN_WIDTH)
            riga.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(riga.german, riga.floor_list)
            german_german = arcade.check_for_collision_with_list(riga.german, riga.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        riga.germans.append(riga.german)

        riga.background = arcade.load_texture("riga.jpg")

    return riga

def city_seven():
    """City of Warsaw"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    warsaw = Europa(None, None, None, None, None, None, None, None)
    warsaw.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        warsaw.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        warsaw.floor.center_x = x
        warsaw.floor.center_y = 216
        warsaw.floor_list.append(warsaw.floor)

    for i in range(len(adolf.troop_list) // 45):
        warsaw.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            warsaw.german.center_x = random.randrange(SCREEN_WIDTH)
            warsaw.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(warsaw.german, warsaw.floor_list)
            german_german = arcade.check_for_collision_with_list(warsaw.german, warsaw.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        warsaw.germans.append(warsaw.german)

        warsaw.background = arcade.load_texture("warsaw.png")

    return warsaw

def city_eight():
    """City of konigsberg"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    konigsberg = Europa(None, None, None, None, None, None, None, None)
    konigsberg.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        konigsberg.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        konigsberg.floor.center_x = x
        konigsberg.floor.center_y = 216
        konigsberg.floor_list.append(konigsberg.floor)

    for i in range(len(adolf.troop_list) // 45):
        konigsberg.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            konigsberg.german.center_x = random.randrange(SCREEN_WIDTH)
            konigsberg.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(konigsberg.german, konigsberg.floor_list)
            german_german = arcade.check_for_collision_with_list(konigsberg.german, konigsberg.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        konigsberg.germans.append(konigsberg.german)

    return konigsberg

def city_nine():
    """City of Kursk"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    kursk = Europa(None, None, None, None, None, None, None, None)
    kursk.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        kursk.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        kursk.floor.center_x = x
        kursk.floor.center_y = 216
        kursk.floor_list.append(kursk.floor)

    for i in range(len(adolf.troop_list) // 45):
        kursk.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            kursk.german.center_x = random.randrange(SCREEN_WIDTH)
            kursk.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(kursk.german, kursk.floor_list)
            german_german = arcade.check_for_collision_with_list(kursk.german, kursk.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        kursk.germans.append(kursk.german)

    return kursk

def city_ten():
    """City of Breslau"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    breslau = Europa(None, None, None, None, None, None, None, None)
    breslau.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        breslau.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        breslau.floor.center_x = x
        breslau.floor.center_y = 216
        breslau.floor_list.append(breslau.floor)

    for i in range(len(adolf.troop_list) // 45):
        breslau.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            breslau.german.center_x = random.randrange(SCREEN_WIDTH)
            breslau.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(breslau.german, breslau.floor_list)
            german_german = arcade.check_for_collision_with_list(breslau.german, breslau.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        breslau.germans.append(breslau.german)

    return breslau

def city_eleven():
    """City of Bucharest"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    bucharest = Europa(None, None, None, None, None, None, None, None)
    bucharest.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        bucharest.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        bucharest.floor.center_x = x
        bucharest.floor.center_y = 216
        bucharest.floor_list.append(bucharest.floor)

    for i in range(len(adolf.troop_list) // 45):
        bucharest.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            bucharest.german.center_x = random.randrange(SCREEN_WIDTH)
            bucharest.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(bucharest.german, bucharest.floor_list)
            german_german = arcade.check_for_collision_with_list(bucharest.german, bucharest.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        bucharest.germans.append(bucharest.german)

    return bucharest

def city_twelve():
    """City of Budapest"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    budapest = Europa(None, None, None, None, None, None, None, None)
    budapest.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        budapest.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        budapest.floor.center_x = x
        budapest.floor.center_y = 216
        budapest.floor_list.append(budapest.floor)

    for i in range(len(adolf.troop_list) // 45):
        budapest.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            budapest.german.center_x = random.randrange(SCREEN_WIDTH)
            budapest.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(budapest.german, budapest.floor_list)
            german_german = arcade.check_for_collision_with_list(budapest.german, budapest.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        budapest.germans.append(budapest.german)

    return budapest

def city_thirteen():
    """City of Prague"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    prague = Europa(None, None, None, None, None, None, None, None)
    prague.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        prague.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        prague.floor.center_x = x
        prague.floor.center_y = 216
        prague.floor_list.append(prague.floor)

    for i in range(len(adolf.troop_list) // 45):
        prague.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            prague.german.center_x = random.randrange(SCREEN_WIDTH)
            prague.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(prague.german, prague.floor_list)
            german_german = arcade.check_for_collision_with_list(prague.german, prague.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        prague.germans.append(prague.german)

    return prague

def city_fourteen():
    """CIty of Stettin"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    stettin = Europa(None, None, None, None, None, None, None, None)
    stettin.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        stettin.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        stettin.floor.center_x = x
        stettin.floor.center_y = 216
        stettin.floor_list.append(stettin.floor)

    for i in range(len(adolf.troop_list) // 45):
        stettin.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            stettin.german.center_x = random.randrange(SCREEN_WIDTH)
            stettin.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(stettin.german, stettin.floor_list)
            german_german = arcade.check_for_collision_with_list(stettin.german, stettin.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        stettin.germans.append(stettin.german)

    return stettin

def city_fifteen():
    """City of Berlin"""
    adolf = text_adventure_files.adolf_hitler.AdolfHitler()
    berlin = Europa(None, None, None, None, None, None, None, None)
    berlin.germans = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        berlin.floor = arcade.Sprite("grass.png", SPRITE_SCALING)
        berlin.floor.center_x = x
        berlin.floor.center_y = 216
        berlin.floor_list.append(berlin.floor)

    for i in range(len(adolf.troop_list) // 40):
        berlin.german = adolf_sprite_ai.Germans("zombie_idle.png", SPRITE_SCALING)
        placed = False
        while not placed:
            """Places a german wherever, if they have not been placed in the ground or on top of each other"""
            berlin.german.center_x = random.randrange(SCREEN_WIDTH)
            berlin.german.bottom = 200

            german_floor_list = arcade.check_for_collision_with_list(berlin.german, berlin.floor_list)
            german_german = arcade.check_for_collision_with_list(berlin.german, berlin.germans)

            if len(german_german) == 0 and len(german_floor_list) == 0:
                placed = True
        berlin.germans.append(berlin.german)

    return berlin