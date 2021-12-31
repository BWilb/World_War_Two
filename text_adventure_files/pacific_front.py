import hirohito
import hirohito_ai
import georgy_zhukov
import PacificLocations
import minorities
import random
import tanks

def initial_soviet_recruitment(georgy):
    """creation of 200,000 to 600,000 soviet soldiers
        and 2,000 to 4,000 T34s
    """
    recruit = (random.randrange(200000, 600000) // 1)
    for i in range(recruit):
        soldier = georgy_zhukov.SovietSoldier()
        georgy.troop_list.append(soldier)

    t34 = (random.randrange(2000, 4000) // 1)
    for i in range(t34):
        tank = tanks.T34Tank()
        georgy.tank_list.append(tank)

def civilian_count(georgy):
    """Creation of 250,000 to 500,000 civilians"""
    civilian = (random.randrange(250000, 500000) // 1)
    for i in range(civilian):
        civ = georgy_zhukov.SovietCivilian()
        georgy.population.append(civ)

def soviet_recruitment(georgy):
    """
    recruitment of 100,000 - 400,000 soldiers
    production of 5,000 to 8,000 T34 tanks"""
    soldiers = (random.randrange(100000, 400000) // 1)
    for i in range(soldiers):
        soldier = georgy_zhukov.SovietSoldier()
        georgy.troop_list.append(soldier)

    crappy = (random.randrange(5000, 8000) // 1)
    for i in range(crappy):
        tank = tanks.T34Tank()
        georgy.tank_list.append(tank)

def initial_japanese_recruitment(hiro_hito):
    """creation of 200,000 - 400,000 japanese troops
    Creation of 4,000 - 600,000 japanese civilians
    """
    bing_bong = (random.randrange(200000, 400000) // 1)
    for i in range(bing_bong):
        bing = hirohito.JapaneseSoldiers()
        hiro_hito.troop_list.append(bing)

    civilian = (random.randrange(4000, 600000) // 1)
    for i in range(civilian):
        civ = hirohito.JapaneseCivilians()
        hiro_hito.population.append(civ)

def japanese_recruitment(hiro_hito):
    bing_bing = (random.randrange(200000, 400000) // 1)
    for i in range(bing_bing):
        japan = hirohito.JapaneseSoldiers()
        hiro_hito.troop_list.append(japan)

def chinese_list(hiro_hito):
    """creation of 250,000 chinese for the japanese to genocide"""
    bing_bing = (random.randrange(200000, 400000) // 1)
    for i in range(bing_bing):
        china = minorities.Chinese()
        hiro_hito.chinese.append(china)

def check_conditions(georgy):
    """Function that for each loop of european or pacific front; checks Zhukov's conditions"""
    if georgy.hunger >= 15:
        print("\nYou need to eat!")
    elif georgy.hunger >= 25:
        print("\nYou have died from hunger")

    if georgy.thirst >= 10:
        print("You need to drink!")
    elif georgy.thirst >= 20:
        print("You have died from dehydration")

    if georgy.health <= 300:
        print("You are in excellent condition")
    elif georgy.health <= 225:
        print("You are in good condition")
    elif georgy.health <= 165:
        print("You are in mild condition")
    elif georgy.health <= 100:
        print("You are in poor condition")
    elif georgy.health <= 50:
        print("You are in horrible condition. Get some sleep")
    elif georgy.health <= 0:
        print("You died")

    if georgy.energy <= 100:
        print("Your energy levels are fine\n")
    elif georgy.energy <= 65:
        print("Your energy levels are moderately full")
    elif georgy.energy <= 40:
        print("Your energy levels are near depletion. Get some sleep.")
    elif georgy.energy <= 0:
        print("You died due to no energy")

def georgy_eat(georgy):
    """Function that is called if user chooses to eat on the european or western front"""
    georgy.hunger = 0
    georgy.energy += random.randrange(1, 10)
    georgy.health += 10
    """binary search through supplies list, for keyword food"""
    key = "food"
    found = False
    lower_bound = 0
    upper_bound = len(georgy.food_list) - 1
    while lower_bound <= upper_bound:
        middle_pos = (lower_bound + upper_bound) // 2
        if georgy.food_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif georgy.food_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
            georgy.food_list.remove(georgy.food_list[middle_pos])
            break
    print("you chose to eat\n")

def georgy_drink(georgy):
    """Function that is called if user chooses to drink on the European or western front"""
    georgy.thirst = 0
    georgy.energy += random.randrange(1, 5)
    georgy.health += 4
    """binary search through supplies list for water"""
    key = "water"
    found = False
    lower_bound = 0
    upper_bound = len(georgy.water_list) - 1
    while lower_bound <= upper_bound:
        middle_pos = (lower_bound + upper_bound) // 2
        if georgy.water_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif georgy.water_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
            georgy.water_list.remove(georgy.water_list[middle_pos])
            break

    print("you chose to drink\n")

def georgy_sleep(georgy):
    """This function handles when the user chooses to sleep"""
    georgy.heatlh = 300
    georgy.energy = 100
    for i in range(len(georgy.troop_list)):
        georgy.troop_list[i].health = 100
    print("you and your military chose to rest")

def pacific_stats(georgy, hirohito):
    """stats for the pacific front"""
    print(f"\nYour energy levels are {georgy.energy} pts")
    print(f"Your health levels are {georgy.health} pts")
    print(f"You have {georgy.hunger} hunger")
    print(f"You have {georgy.thirst} thirst")
    print(f"You have {len(georgy.troop_list)} soldiers left")
    print(f"You have {len(georgy.tank_list)} T34s left")
    print(f"You have {len(georgy.food_list)} items of food left")
    print(f"You have {len(georgy.water_list)} items of water left")
    print(f"You have killed {georgy.score_card} japanese civilians and soldiers")
    print(f"There are {len(hirohito.troop_list)} japanese troops left")
    print(f"There are {len(hirohito.chinese)} chinese left")
    print(f"There are {len(hirohito.population)} japanese civilians left")
    print(f"Hirohito has killed {hirohito.score_card} civilians\n")

def commit_japanese_genocide(georgy, hiro_hito):
    """1. Function if you want to commit genocide
        2. Hirohito's population adds 5,000 - 500,000 after each genocidal round
        """
    print("you are committing genocide")
    kill = 0

    kills = random.randrange(len(hiro_hito.population) // 5)
    for genocide in range(kills):
        hiro_hito.population[genocide].health -= random.randrange(kills)
        if hiro_hito.population[genocide].health <= 0:
            hiro_hito.population.remove(hiro_hito.population[genocide])
            kill += 1
            georgy.score_card += 1

    print(f"You killed {kill} japanese civilians")
    additions = random.randrange(5000, 500000)
    for i in range(additions):
        add = hirohito.JapaneseCivilians()
        hiro_hito.population.append(add)

def random_events(georgy, hirohito):
    """collection of random events
        1. running across german military units
        2. running across more food
        3. running across more water
    """
    japanese_army_sizes = ["batallion",
                         "division",
                         "army group"]

    if georgy.distance % 20 == 2:
        """random event set for running across german units
        if distance has a remainder of 2 when divided by 20 this happens
        """
        japanese_military = random.randrange(len(japanese_army_sizes) // 1)

        if japanese_military == 1:
            """German battalion"""
            kills = 0
            print("you have come across a german battalion")
            german_size = (random.randrange(400, 100) // 1)
            for attack in range(german_size):
                hirohito.troop_list[attack].health -= random.randrange(0, 251)
                if hirohito.troop_list[attack].health <= 0:
                    hirohito.troop_list.remove(hirohito.troop_list[attack])
                    georgy.score_card += 1
                    kills += 1
            print(f"you killed {kills} germans\n")

        elif japanese_military == 2:
            """German division"""
            print("you have come across a german division")
            kills = 0
            german_size = (random.randrange(10000, 15000) // 1)
            for attack in range(german_size):
                hirohito.troop_list[attack].health -= random.randrange(0, 251)
                if hirohito.troop_list[attack].health <= 0:
                    hirohito.troop_list.remove(hirohito.troop_list[attack])
                    georgy.score_card += 1
                    kills += 1
                    print(f"you killed {kills} germans\n")

        elif japanese_military == 3:
            """German army group"""
            print("you have come across a german army group")
            kills = 0
            german_size = (random.randrange(100000, 150000) // 1)
            for attack in range(german_size):
                hirohito.troop_list[attack].health -= random.randrange(0, 251)
                if hirohito.troop_list[attack].health <= 0:
                    hirohito.troop_list.remove(hirohito.troop_list[attack])
                    georgy.score_card += 1
                    kills += 1
                    print(f"you killed {kills} germans\n")

    elif georgy.distance % 5 == 4:
        """Acquiring food provisions"""
        print("you have come across more food provisions.")
        answer = input("Do you want to acquire these provisions?: ")
        if answer.lower() == "y" or answer.lower() == "yes":
            georgy.food_list.append("food")

    elif georgy.distance % 4 == 3:
        """Acquiring water provision"""
        print("you have come across more water provisions")
        answer = input("Do you want to acquire these provisions?: ")
        if answer.lower() == "y" or answer.lower() == "yes":
            georgy.water_list.append("water")

def vdladivostok_game_version(georgy, hiro_hito):
    """Logic for the Pacific theatre"""
    choices = ["\n1. Move",
               "2. Eat",
               "3. Drink",
               "4. rest",
               "5. Quit",
               "6. Check Stats",
               "7. Commit Genocide\n"]

    georgy.pacific_locations = PacificLocations.locations()
    directions = ["\n1. North",
                  "2. North East",
                  "3. East",
                  "4. South East",
                  "5. South",
                  "6. South West",
                  "7. West",
                  "8. North West\n"]
    current_city = 0
    alive = False
    choice = None
    while not alive:
        """This while loop keeps looping until Zhukov dies, quits, or runs out of troops"""
        print(georgy.pacific_locations[current_city].description)
        for i in range(len(choices)):
            """prints out Zhukov's possible choices"""
            print(choices[i])
        first_choice = int(input("what is your choice?: "))
        if first_choice == 1:
            georgy.health -= random.randrange(1, 25)
            georgy.energy -= random.randrange(4, 10)
            georgy.energy -= random.randrange(4, 8)

            for i in range(len(directions)):
                """prints out the specific directions Zhukov could take"""
                print(directions[i])

            choice = int(input("which direction do you choose? Remember there are only the specific ones: "))
            if choice == 1:
                """Choice if you happen to choose to go north"""
                next_city = georgy.pacific_locations[current_city].north
                if georgy.pacific_locations[current_city].north is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += random.randrange(300, 4000)

            elif choice == 2:
                """Choice if you happen to choose to go north east"""
                next_city = georgy.pacific_locations[current_city].north_east
                if georgy.pacific_locations[current_city].north_east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += random.randrange(300, 4000)

            elif choice == 3:
                """Choice if you happen to choose to go east"""
                next_city = georgy.pacific_locations[current_city].east
                if georgy.pacific_locations[current_city].east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += random.randrange(300, 4000)

            elif choice == 4:
                """Choice if you happen to choose to go south east"""
                next_city = georgy.pacific_locations[current_city].south_east
                if georgy.pacific_locations[current_city].south_east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += random.randrange(300, 4000)

            elif choice == 5:
                """Choice if you happen to choose to go south"""
                next_city = georgy.pacific_locations[current_city].south
                if georgy.pacific_locations[current_city].south is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += random.randrange(300, 4000)

            elif choice == 6:
                """Choice if you happen to choose to go south west"""
                next_city = georgy.pacific_locations[current_city].south_west
                if georgy.pacific_locations[current_city].south_west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += random.randrange(300, 4000)

            elif choice == 7:
                """Choice if you happen to choose to go west"""
                next_city = georgy.pacific_locations[current_city].west
                if georgy.pacific_locations[current_city].west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += random.randrange(300, 4000)

            elif choice == 8:
                """Choice if you happen to choose to go north west"""
                next_city = georgy.pacific_locations[current_city].north_west
                if georgy.pacific_locations[current_city].north_west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += random.randrange(300, 4000)

            else:
                """Last else statement covers an incorrect choice"""
                print("That choice is invalid; try again.\n")

        elif first_choice == 2:
            """reducing hunger"""
            georgy_eat(georgy)

        elif first_choice == 3:
            """reducing thirst"""
            georgy_drink(georgy)

        elif first_choice == 4:
            """increasing health and energy"""
            georgy_sleep(georgy)

        elif first_choice == 5:
            """quitting"""
            print("You have committed suicide Georgy. Goodbye")
            alive = True

        elif first_choice == 6:
            pacific_stats(georgy, hiro_hito)

        elif first_choice == 7:
            commit_japanese_genocide(georgy, hiro_hito)

        else:
            print("Are you blind???? Look at the options\n")
        hirohito_ai.main()
        check_conditions(georgy)
        soviet_recruitment(georgy)
        japanese_recruitment(hiro_hito)
        random_events(georgy, hiro_hito)

def main():
    georgy = georgy_zhukov.GeorgyZhukov()
    """Creation of zhukov object"""
    initial_soviet_recruitment(georgy)

    hiro_hito = hirohito.Hirohito()
    """Creation of hiro_hito object"""
    initial_japanese_recruitment(hiro_hito)
    chinese_list(hiro_hito)
    vdladivostok_game_version(georgy, hiro_hito)