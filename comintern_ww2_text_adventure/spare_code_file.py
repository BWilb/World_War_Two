from text_adventure_files import eastern_european_front
import pacific_front

def main():
    question_one = False
    question_two = False
    question_three = False
    game_version = ["1. Text Adventure Version",
                    "2. Sprite Version"]
    choices = ["1. European",
               "2. Pacific\n"]
    """Initialization of three loop control variables and choice variable, where user can choose 
    which front they want.
    The user can also choose if they want to play text adventure or a sprite game.
    """

    while not question_one:
        for i in range(len(game_version)):
            print(game_version[i])
        choice = int(input("what is your choice?: "))
        if choice == 1:
            print("you have selected text adventure...")

            while not question_two:
                print("The year is 1941. Germany and Japan have just declared war on Soviet Russia. The motherland"
                      " has called you to fight by her side.\n")
                answer = input("do you accept her invitation?: ")

                if answer.lower() == "y" or answer.lower() == "yes":
                    print("Huzzah, you have possibly saved Soviet Russia from ever greater suffering.\n")
                    question_two = True

                    for i in range(len(choices)):
                        """12/21 I did not expect that I would have to create this for loop in order to bypass the try block
                        12/21 update: I removed the try blocks
                        """
                        print(choices[i])

                    while not question_three:
                        """loop that captures which front you would like to fight in"""
                        answer = int(input("Which theatre do you want to fight in?: "))
                        if answer == 1:
                            print("transferring to Moscow\n")
                            eastern_european_front.main()
                            question_three = True

                        elif answer == 2:
                            print("transferring to Vdladivostok\n")
                            pacific_front.main()
                            question_three = True

                        else:
                            print("?????. You're supposed to only answer with a one or two\n")

                elif answer.lower() == "n" or answer.lower() == "no":
                    """breaks out of the 2nd loop"""
                    print("The Soviets are doomed\n"
                          "Good bye.")
                    break
        elif choice == 2:
            print("the sprite version has not yet been developed.")
main()