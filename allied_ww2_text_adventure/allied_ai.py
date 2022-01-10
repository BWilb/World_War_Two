import allied_classes
import random

def allied_ww2():
    allied_ais = []
    charles_gaulle = allied_classes.CharlesDeGaulle()
    allied_ais.append(charles_gaulle)

    fdr = allied_classes.FDR()
    allied_ais.append(fdr)

    churchill = allied_classes.WinstonChurchill()
    allied_ais.append(churchill)

    front_choices = ["European",
                     "Pacific"]
    choice = random.randrange(len(front_choices))

    ai_choice = random.randrange(len(allied_ais))
    if ai_choice == 1:
        """If randomized choice is French"""
        print("The allied ai has chosen Charles De Gaulle.\n")
        if choice == 1:
            print("Transferring to London.\n"
                  "A Free French force will soon land on Normandy Beach!")
        elif choice == 2:
            print("Transferring to Delhi India")

    elif ai_choice == 2:
        """If randomized choice is American"""
        print("The allied ai has chosen FDR.\n"
              "The United States has joined the war!")
        if choice == 1:
            print("Transferring to London.\n"
                  "An American force will soon land on Normandy Beach!")
        elif choice == 2:
            print("Transferring to Pearl Harbor")

    elif ai_choice == 3:
        """If randomized choice is British"""
        print("The allied ai has chosen Winston Churchill.\n"
              "The Brits won over the air war...but for how long?")
        print("Transferring to London.")