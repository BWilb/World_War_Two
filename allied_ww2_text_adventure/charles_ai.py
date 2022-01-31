import allied_classes
import comintern_ww2_text_adventure
import random

def charles_ww2(charles):
    choices = ["\n1. Move",
               "2. Eat",
               "3. Drink",
               "4. Rest",
               "5. Quit",
               "6. View Stats",
               "7. Commit Genocide\n"]
    charles.locations = comintern_ww2_text_adventure.EasternEuropeanLocations.cities()
    directions = ["\n1. North",
                  "2. North East",
                  "3. East",
                  "4. South East",
                  "5. South",
                  "6. South West",
                  "7. West",
                  "8. North West\n"]
    charles.current_location = 0
    alive = False
    choice = None
    while not alive:
        """This while loop keeps looping until FDR dies, quits, or runs out of troops.
                decides to that is."""
        choice = random.randrange(len(choices) // 1)
        if choice == 1:
            charles.health -= (random.randrange(1, 45) // 1)
            directional_choice = random.randrange(len(directions) // 1)
            """randomized directional choice"""
            if directional_choice == 1:
                next_city = charles.locations[charles.current_city].north
                if charles.locations[charles.current_city].north is None:
                    print("FDR wasn't able to move. Hurrah.\n")
                else:
                    charles.current_city = next_city

            elif directional_choice == 2:
                next_city = charles.locations[charles.current_city].north_east
                if charles.locations[charles.current_city].north_east is None:
                    print("FDR wasn't able to move. Hurrah\n")
                else:
                    charles.current_city = next_city

            elif directional_choice == 3:
                """Choice if you happen to choose to go east"""
                next_city = charles.locations[charles.current_city].east
                if charles.locations[charles.current_city].east is None:
                    print("FDR wasn't able to move\n")
                else:
                    charles.current_city = next_city

            elif directional_choice == 4:
                """Choice if you happen to choose to go south east"""
                next_city = charles.locations[charles.current_city].south_east
                if charles.locations[charles.current_city].south_east is None:
                    print("FDR wasn't able to move.\n")
                else:
                    charles.current_city = next_city

            elif directional_choice == 5:
                """Choice if you happen to choose to go south"""
                next_city = charles.locations[charles.current_city].south
                if charles.locations[charles.current_city].south is None:
                    print("FDR wasn't able to move.\n")
                else:
                    charles.current_city = next_city

            elif directional_choice == 6:
                """Choice if you happen to choose to go south west"""
                next_city = charles.locations[charles.current_city].south_west
                if charles.locations[charles.current_city].south_west is None:
                    print("FDR wasn't able to move.\n")
                else:
                    charles.current_city = next_city

            elif directional_choice == 7:
                """Choice if you happen to choose to go west"""
                next_city = charles.locations[charles.current_city].west
                if charles.locations[charles.current_city].west is None:
                    print("FDR wasn't able to move.\n")
                else:
                    charles.current_city = next_city

            elif directional_choice == 8:
                """Choice if you happen to choose to go north west"""
                next_city = charles.locations[charles.current_city].north_west
                if charles.locations[charles.current_city].north_west is None:
                    print("FDR wasn't able to move.\n")
                else:
                    charles.current_city = next_city
            alive = True
def main():
    charles = allied_classes.CharlesDeGaulle()
    charles_ww2(charles)