import random
import EasternEuropeanLocations
import tanks
import minorities

"""In this file, you don't control anything. This file controls Adolf Hitler's AI.
Here Zhukov's mission can be made or broken. 
Adolf's current city is currently set in Moscow, later on it will be set to Berlin as
I update this game
"""

def adolf_ww2_version(adolf, georgy):
    """Main function that controls Hitler"""
    choices = ["1. Move",
               "2. Commit Genocide",
               "3. Improve tank production",
               "4. Increase propaganda measures",
               "5. Initiate"]
    adolf.locations = EasternEuropeanLocations.cities()
    directions = ["1. North",
                  "2. North East",
                  "3. East",
                  "4. South East",
                  "5. South",
                  "6. South West",
                  "7. West",
                  "8. North West"]
    adolf.current_city = 0
    alive = False
    while not alive:
        choice = random.randrange(len(choices) // 1)
        """choice variable controls what Hitler's decision will be
        Hitler acted in a random manner in reality anyway
        """
        if choice == 1:
            adolf.health -= (random.randrange(1, 45) // 1)
            directional_choice = random.randrange(len(directions) // 1)
            """randomized directional choice"""
            if directional_choice == 1:
                next_city = adolf.locations[adolf.current_city].north
                if adolf.locations[adolf.current_city].north is None:
                    print("Adolf wasn't able to move. Hurrah.\n")
                else:
                    adolf.current_city = next_city

            elif directional_choice == 2:
                next_city = adolf.locations[adolf.current_city].north_east
                if adolf.locations[adolf.current_city].north_east is None:
                    print("Adolf wasn't able to move. Hurrah\n")
                else:
                    adolf.current_city = next_city

            elif directional_choice == 3:
                """Choice if you happen to choose to go east"""
                next_city = adolf.locations[adolf.current_city].east
                if adolf.locations[adolf.current_city].east is None:
                    print("Adolf wasn't able to move\n")
                else:
                    adolf.current_city = next_city

            elif directional_choice == 4:
                """Choice if you happen to choose to go south east"""
                next_city = adolf.locations[adolf.current_city].south_east
                if adolf.locations[adolf.current_city].south_east is None:
                    print("Adolf wasn't able to move.\n")
                else:
                    adolf.current_city = next_city

            elif directional_choice == 5:
                """Choice if you happen to choose to go south"""
                next_city = adolf.locations[adolf.current_city].south
                if adolf.locations[adolf.current_city].south is None:
                    print("Adolf wasn't able to move.\n")
                else:
                    adolf.current_city = next_city

            elif directional_choice == 6:
                """Choice if you happen to choose to go south west"""
                next_city = adolf.locations[adolf.current_city].south_west
                if adolf.locations[adolf.current_city].south_west is None:
                    print("Adolf wasn't able to move.\n")
                else:
                    adolf.current_city = next_city

            elif directional_choice == 7:
                """Choice if you happen to choose to go west"""
                next_city = adolf.locations[adolf.current_city].west
                if adolf.locations[adolf.current_city].west is None:
                    print("Adolf wasn't able to move.\n")
                else:
                    adolf.current_city = next_city

            elif directional_choice == 8:
                """Choice if you happen to choose to go north west"""
                next_city = adolf.locations[adolf.current_city].north_west
                if adolf.locations[adolf.current_city].north_west is None:
                    print("Adolf wasn't able to move.\n")
                else:
                    adolf.current_city = next_city
            alive = True

        elif choice == 2:
            kill = 0
            if len(adolf.jews) >= 0:
                print("\nHitler is committing genocide")
                kills = (len(adolf.jews) // 10)
                for i in range(kills):
                    adolf.jews[i].health -= random.randrange(550)
                    if adolf.jews[i].health <= 0:
                        adolf.jews.remove(adolf.jews[i])
                        adolf.score_card += 1
                        kill += 1
                print(f"Hitler killed {kill} jews\n")
            elif len(adolf.jews) <= 0:
                print("Hitler ran out of jews to kill\n")

            addition = random.randrange(5, 50000)
            for i in range(addition):
                jew = minorities.Jew()
                adolf.jews.append(jew)

            break

        elif choice == 3:
            production = 3000
            for i in range(production):
                tank = tanks.TigerTank()
                adolf.tank_list.append(tank)
            print("Hitler has just improved his tank production\n")
            break

        elif choice == 4:
            adolf.troop_list *= 2
            print("Hitler has just improved his propaganda measures\n")
            break

def main(georgy, adolf):
    adolf_ww2_version(adolf, georgy)