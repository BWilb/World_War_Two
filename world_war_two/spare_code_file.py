import adolf_hitler
import EuropeanLocations
import georgy_zhukov
import hirohito
import minorities
import PacificLocations
import random
import tanks

def recruitment(georgy):
    """creation of 2000 to 6000 soviet soldiers"""
    recruit = (random.randrange(200000, 600000) // 1)
    for i in range(recruit):
        soldier = georgy_zhukov.SovietSoldier()
        georgy.troop_list.append(soldier)

def civilian_count(georgy):
    """Creation of 250,000 to 500,000 civilians"""
    civilian = (random.randrange(250000, 500000) // 1)
    for i in range(civilian):
        civ = georgy_zhukov.SovietCivilian()
        georgy.population.append(civ)

def t34(georgy):
    """creation of 200 to 600 T34 tanks"""
    crappy = (random.randrange(5000, 8000) // 1)
    for i in range(crappy):
        tank = tanks.T34Tank()
        georgy.tank_list.append(tank)

def german_troops(adolf):
    """initialization of 100000 to 200000 german troops"""
    rand = (random.randrange(300000, 500000) // 1)
    for i in range(rand):
        soldier = adolf_hitler.GermanSoldier()
        adolf.troop_list.append(soldier)

    civilians = random.randrange(6000, 500000)
    for i in range(civilians):
        civ = adolf_hitler.GermanCivilian()
        adolf.population.append(civ)

def german_resupply(adolf):
    german_recruitments = random.randrange(1, 4000)
    for i in range(german_recruitments):
        gerry = adolf_hitler.GermanSoldier()
        adolf.troop_list.append(gerry)

def tigers(adolf):
    """creation of 100 to 400 tiger tanks"""
    tank = (random.randrange(4000, 6000) // 1)
    for i in range(tank):
        tiger = tanks.TigerTank()
        adolf.tank_list.append(tiger)

def jew_list(adolf):
    """creation of 500,000 jews"""
    ash = 500000
    for i in range(ash):
        jew = minorities.Jew()
        adolf.jews.append(jew)

def japanese_troops(hiro_hito):
    """creation of 5,000 - 6,000 japanese troops
    Creation of 4,000 - 600,000 japanese civilians
    """
    bing_bong = (random.randrange(5000, 6000) // 1)
    for i in range(bing_bong):
        bing = hirohito.JapaneseSoldiers()
        hiro_hito.troop_list.append(bing)

    civilian = (random.randrange(4000, 600000) // 1)
    for i in range(civilian):
        civ = hirohito.JapaneseCivilians()
        hiro_hito.population.append(civ)

def chinese_list(hiro_hito):
    """creation of 250,000 chinese for the japanese to genocide"""
    bing_bing = 250000
    for i in range(bing_bing):
        china = minorities.Chinese()
        hiro_hito.chinese.append(china)

def random_events(georgy, adolf):
    """collection of random events
        1. running across german military units
        2. running across more food
        3. running across more water
    """
    german_army_sizes = ["batallion",
                         "division",
                         "army group"]

    if georgy.distance % 20 == 2:
        """random event set for running across german units
        if distance has a remainder of 2 when divided by 20 this happens
        """
        german_military = random.randrange(len(german_army_sizes) // 1)

        if german_military == 1:
            """German battalion"""
            kills = 0
            print("you have come across a german battalion")
            german_size = (random.randrange(400, 100) // 1)
            for attack in range(german_size):
                adolf.troop_list[attack].health -= random.randrange(0, 251)
                if adolf.troop_list[attack].health <= 0:
                    adolf.troop_list.remove(adolf.troop_list[attack])
                    georgy.score_card += 1
                    kills += 1
            print(f"you killed {kills} germans")

        elif german_military == 2:
            """German division"""
            print("you have come across a german division")
            kills = 0
            german_size = (random.randrange(10000, 15000) // 1)
            for attack in range(german_size):
                adolf.troop_list[attack].health -= random.randrange(0, 251)
                if adolf.troop_list[attack].health <= 0:
                    adolf.troop_list.remove(adolf.troop_list[attack])
                    georgy.score_card += 1
                    kills += 1
                    print(f"you killed {kills} germans")

        elif german_military == 3:
            """German army group"""
            print("you have come across a german army group")
            kills = 0
            german_size = (random.randrange(100000, 150000) // 1)
            for attack in range(german_size):
                adolf.troop_list[attack].health -= random.randrange(0, 251)
                if adolf.troop_list[attack].health <= 0:
                    adolf.troop_list.remove(adolf.troop_list[attack])
                    georgy.score_card += 1
                    kills += 1
                    print(f"you killed {kills} germans")

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

def european_stats(georgy, adolf):
    german = 0
    for i in range(len(adolf.troop_list)):
        german += 1

    print(f"\nYour energy levels are {georgy.energy} pts")
    print(f"Your health levels are {georgy.health} pts")
    print(f"You have {georgy.hunger} hunger")
    print(f"You have {georgy.thirst} thirst")
    print(f"You have {len(georgy.troop_list)} soldiers left")
    print(f"You have {len(georgy.tank_list)} T34s left")
    print(f"You have {len(georgy.food_list)} items of food left")
    print(f"You have {len(georgy.water_list)} items of water left")
    print(f"There are {len(adolf.troop_list)} german troops left")
    print(f"There are {len(adolf.tank_list)} Tiger tanks left")
    print(f"You have killed {georgy.score_card} germans")
    print(f"There are {len(adolf.jews)} jews left")
    print(f"There are {len(adolf.population)} german civilians left\n")

def commit_german_genocide(georgy, adolf):
    """1. Function if you want to commit genocide
    2. Adolf's population never runs out
    """
    print("you are committing genocide")
    kill = 0

    kills = random.randrange(len(adolf.population) // 10)
    for genocide in range(kills):
        adolf.population[genocide].health -= random.randrange(kills)
        if adolf.population[genocide].health <= 0:
            adolf.population.remove(adolf.population[genocide])
            kill += 1
            georgy.score_card += 1

    print(f"You killed {kill} german civilians")
    additions = random.randrange(5000, 500000)
    for i in range(additions):
        add = adolf_hitler.GermanCivilian()
        adolf.population.append(add)

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
        print("Your energy levels are fine")
    elif georgy.energy <= 65:
        print("Your energy levels are moderately full")
    elif georgy.energy <= 40:
        print("Your energy levels are near depletion. Get some sleep.")
    elif georgy.energy <= 0:
        print("You died due to no energy")

def moscow_game_version(georgy, adolf):
    """This function handles the European front of the game"""
    choices = ["\n1. Move",
               "2. Eat",
               "3. Drink",
               "4. Rest",
               "5. Quit",
               "6. View Stats",
               "7. Commit Genocide\n"]
    europe_cities = EuropeanLocations.cities()
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
        print(europe_cities[current_city].description)
        for i in range(len(choices)):
            """prints out Zhukov's possible choices"""
            print(choices[i])

        first_choice = int(input("what is your choice?: "))
        if first_choice == 1:
            georgy.heatlh -= (random.randrange(1, 25) // 1)
            georgy.energy -= (random.randrange(4, 10) // 1)
            georgy.thirst += (random.randrange(1, 5) // 1)
            georgy.hunger += (random.randrange(1, 10) // 1)

            for i in range(len(directions)):
                """prints out the specific directions Zhukov could take"""
                print(directions[i])

            choice = int(input("which direction do you choose? Remember there are only the specific ones: "))
            if choice == 1:
                """Choice if you happen to choose to go north"""
                next_city = europe_cities[current_city].north
                if europe_cities[current_city].north is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += (random.randrange(1000, 5000) // 1)
                    random_events(georgy, adolf)

            elif choice == 2:
                """Choice if you happen to choose to go north east"""
                next_city = europe_cities[current_city].north_east
                if europe_cities[current_city].north_east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += (random.randrange(1000, 5000) // 1)
                    random_events(georgy, adolf)

            elif choice == 3:
                """Choice if you happen to choose to go east"""
                next_city = europe_cities[current_city].east
                if europe_cities[current_city].east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += (random.randrange(1000, 5000) // 1)
                    random_events(georgy, adolf)

            elif choice == 4:
                """Choice if you happen to choose to go south east"""
                next_city = europe_cities[current_city].south_east
                if europe_cities[current_city].south_east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += (random.randrange(1000, 5000) // 1)
                    random_events(georgy, adolf)

            elif choice == 5:
                """Choice if you happen to choose to go south"""
                next_city = europe_cities[current_city].south
                if europe_cities[current_city].south is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += (random.randrange(1000, 5000) // 1)
                    random_events(georgy, adolf)

            elif choice == 6:
                """Choice if you happen to choose to go south west"""
                next_city = europe_cities[current_city].south_west
                if europe_cities[current_city].south_west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += (random.randrange(1000, 5000) // 1)
                    random_events(georgy, adolf)

            elif choice == 7:
                """Choice if you happen to choose to go west"""
                next_city = europe_cities[current_city].west
                if europe_cities[current_city].west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += (random.randrange(1000, 5000) // 1)
                    random_events(georgy, adolf)

            elif choice == 8:
                """Choice if you happen to choose to go north west"""
                next_city = europe_cities[current_city].north_west
                if europe_cities[current_city].north_west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
                    georgy.distance += (random.randrange(1000, 5000) // 1)
                    random_events(georgy, adolf)
            else:
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
            european_stats(georgy, adolf)

        elif first_choice == 7:
            commit_german_genocide(georgy, adolf)

        else:
            print("Are you blind???? Look at the options")

        check_conditions(georgy)
        german_resupply(adolf)

def vdladivostok_game_version(georgy, hirohito):
    """Logic for the Pacific theatre"""
    choices = ["\n1. Move",
               "2. Eat",
               "3. Drink",
               "4. rest",
               "5. Quit",
               "6. Check Stats",
               "7. Commit Genocide\n"]
    pacific_cities = PacificLocations.locations()
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
        print(pacific_cities[current_city].description)
        for i in range(len(choices)):
            """prints out Zhukov's possible choices"""
            print(choices[i])

        first_choice = int(input("what is your choice?: "))
        if first_choice == 1:
            georgy.heatlh -= random.randrange(1, 25)
            georgy.energy -= random.randrange(4, 10)
            georgy.energy -= random.randrange(4, 8)

            for i in range(len(directions)):
                """prints out the specific directions Zhukov could take"""
                print(directions[i])

            choice = int(input("which direction do you choose? Remember there are only the specific ones: "))
            if choice == 1:
                """Choice if you happen to choose to go north"""
                next_city = pacific_cities[current_city].north
                if pacific_cities[current_city].north is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city

            elif choice == 2:
                """Choice if you happen to choose to go north east"""
                next_city = pacific_cities[current_city].north_east
                if pacific_cities[current_city].north_east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city

            elif choice == 3:
                """Choice if you happen to choose to go east"""
                next_city = pacific_cities[current_city].east
                if pacific_cities[current_city].east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city

            elif choice == 4:
                """Choice if you happen to choose to go south east"""
                next_city = pacific_cities[current_city].south_east
                if pacific_cities[current_city].south_east is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city

            elif choice == 5:
                """Choice if you happen to choose to go south"""
                next_city = pacific_cities[current_city].south
                if pacific_cities[current_city].south is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city

            elif choice == 6:
                """Choice if you happen to choose to go south west"""
                next_city = pacific_cities[current_city].south_west
                if pacific_cities[current_city].south_west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city

            elif choice == 7:
                """Choice if you happen to choose to go west"""
                next_city = pacific_cities[current_city].west
                if pacific_cities[current_city].west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city

            elif choice == 8:
                """Choice if you happen to choose to go north west"""
                next_city = pacific_cities[current_city].north_west
                if pacific_cities[current_city].north_west is None:
                    print("Oh no...You can't go that way. Next time read the description.\n")
                else:
                    current_city = next_city
            else:
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

        else:
            print("Are you blind???? Look at the options")

        check_conditions(georgy)

def main():
    question_one = False
    question_two = False
    choices = ["1. European",
               "2. Pacific\n"]
    """Initialization of three loop control variables and location"""

    georgy = georgy_zhukov.GeorgyZhukov()
    recruitment(georgy)
    t34(georgy)
    civilian_count(georgy)
    """1. Establishment of object georgy based off of class GeorgyZhukov
    2. creation of random amount of soldiers based between 2000 and 6000
    3. creation of 200 to 600 T34 tanks
    4. creation of random amount of civilians
    """
    while not question_one:
        print("The year is 1941. Germany and Japan have just declared war on Soviet Russia. The motherland"
              " has called you to fight by her side.\n")
        answer = input("do you accept her invitation?: ")

        if answer.lower() == "y":
            print("Huzzah, you have possibly saved Soviet Russia from ever greater suffering.\n")
            question_one = True

            for i in range(len(choices)):
                """12/21 I did not expect that I would have to create this for loop in order to bypass the try block
                12/21 update: I removed the try blocks
                """
                print(choices[i])

            while not question_two:
                """loop that captures which front you would like to fight in"""
                answer = int(input("Which theatre do you want to fight in?: "))
                if answer == 1:
                    print("transferring to Moscow\n")
                    adolf = adolf_hitler.AdolfHitler()
                    german_troops(adolf)
                    tigers(adolf)
                    jew_list(adolf)
                    """1. Establishment of object adolf based off of class AdolfHitler
                       2. creation of 3000 to 8000 german troops
                       3. creation of 100 to 400 Tiger tanks
                       4. creation of 500,000 jews
                    """
                    moscow_game_version(georgy, adolf)
                    question_two = True

                elif answer == 2:
                    print("transferring to Vdladivostok\n")
                    hiro_hito = hirohito.Hirohito()
                    japanese_troops(hiro_hito)
                    chinese_list(hiro_hito)
                    vdladivostok_game_version(georgy, hiro_hito)
                    question_two = True

                else:
                    print("?????. You're supposed to only answer with a one or two\n")

        elif answer.lower() == "n":
            """breaks out of the 2nd loop"""
            print("The Soviets are doomed\n"
                  "Good bye.")
            break

main()