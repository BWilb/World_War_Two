import random

import PacificLocations
import minorities


"""In this file, you don't control anything. This file controls Hirohito's AI.
Here Zhukov's mission can be made or broken. 
"""

def hirohito_ww2_version(hiro_hito, georgy):
    """Main function that controls Hitler"""
    choices = ["1. Move",
               "2. Commit Genocide",
               "3. Improve propaganda"]
    hiro_hito.locations = PacificLocations.locations()
    directions = ["1. North",
                  "2. North East",
                  "3. East",
                  "4. South East",
                  "5. South",
                  "6. South West",
                  "7. West",
                  "8. North West"]
    hiro_hito.current_city = 8
    alive = False
    choice = None
    while not alive:
        choice = random.randrange(len(choices) // 1)
        """choice variable controls what Hitler's decision will be
        Hitler acted in a random manner in reality anyway
        """
        if choice == 1:
            hiro_hito.health -= (random.randrange(1, 45) // 1)
            directional_choice = random.randrange(len(directions) // 1)
            """randomized directional choice"""
            if directional_choice == 1:
                next_city = hiro_hito.locations[hiro_hito.current_city].north
                if hiro_hito.locations[hiro_hito.current_city].north is None:
                    print("Hirohito wasn't able to move. Hurrah.\n")
                else:
                    hiro_hito.current_city = next_city

            elif directional_choice == 2:
                next_city = hiro_hito.locations[hiro_hito.current_city].north_east
                if hiro_hito.locations[hiro_hito.current_city].north_east is None:
                    print("Hirohito wasn't able to move. Hurrah\n")
                else:
                    hiro_hito.current_city = next_city

            elif directional_choice == 3:
                """Choice if you happen to choose to go east"""
                next_city = hiro_hito.locations[hiro_hito.current_city].east
                if hiro_hito.locations[hiro_hito.current_city].east is None:
                    print("Hirohito wasn't able to move.\n")
                else:
                    hiro_hito.current_city = next_city

            elif directional_choice == 4:
                """Choice if you happen to choose to go south east"""
                next_city = hiro_hito.locations[hiro_hito.current_city].south_east
                if hiro_hito.locations[hiro_hito.current_city].south_east is None:
                    print("Hirohito wasn't able to move.\n")
                else:
                    hiro_hito.current_city = next_city

            elif directional_choice == 5:
                """Choice if you happen to choose to go south"""
                next_city = hiro_hito.locations[hiro_hito.current_city].south
                if hiro_hito.locations[hiro_hito.current_city].south is None:
                    print("Hirohito wasn't able to move.\n")
                else:
                    hiro_hito.current_city = next_city

            elif directional_choice == 6:
                """Choice if you happen to choose to go south west"""
                next_city = hiro_hito.locations[hiro_hito.current_city].south_west
                if hiro_hito.locations[hiro_hito.current_city].south_west is None:
                    print("Hirohito wasn't able to move.\n")
                else:
                    hiro_hito.current_city = next_city

            elif directional_choice == 7:
                """Choice if you happen to choose to go west"""
                next_city = hiro_hito.locations[hiro_hito.current_city].west
                if hiro_hito.locations[hiro_hito.current_city].west is None:
                    print("Hirohito wasn't able to move.\n")
                else:
                    hiro_hito.current_city = next_city

            elif directional_choice == 8:
                """Choice if you happen to choose to go north west"""
                next_city = hiro_hito.locations[hiro_hito.current_city].north_west
                if hiro_hito.locations[hiro_hito.current_city].north_west is None:
                    print("Hirohito wasn't able to move.\n")
                else:
                    hiro_hito.current_city = next_city
            break

        elif choice == 2:
            kill = 0
            if len(hiro_hito.chinese) >= 0:
                print("Hirohito is committing genocide\n")
                kills = (len(hiro_hito.chinese) // 10)
                for genocide in range(kills):
                    hiro_hito.chinese[genocide].health -= random.randrange(150)
                    print(genocide)
                    print(hiro_hito.chinese[genocide].health)
                    if hiro_hito.chinese[genocide].health <= 0:
                        hiro_hito.chinese.remove(hiro_hito.chinese[genocide])
                        hiro_hito.score_card += 1
                        kill += 1
            elif len(hiro_hito.chinese) <= 0:
                print("Hirohito ran out of chinese to kill")

            print(f"Hirohito killed {kill} chinese")

            addition = random.randrange(40, 60000)
            for i in range(addition):
                chinese = minorities.Chinese()
                hiro_hito.chinese.append(chinese)

            break

        elif choice == 3:
            hiro_hito.troop_list *= 2
            print("Hirohito has just improved his propaganda measures\n")
            break

def main(hiro_hito, zhukov):
    hirohito_ww2_version(hiro_hito, zhukov)