import eastern_european_front
import pacific_front

def main():
    question_one = False
    question_two = False
    choices = ["1. European",
               "2. Pacific\n"]
    """Initialization of two loop control variables and location"""

    while not question_one:
        print("The year is 1941. Germany and Japan have just declared war on Soviet Russia. The motherland"
              " has called you to fight by her side.\n")
        answer = input("do you accept her invitation?: ")

        if answer.lower() == "y" or answer.lower() == "yes":
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
                    eastern_european_front.main()
                    question_two = True

                elif answer == 2:
                    print("transferring to Vdladivostok\n")
                    pacific_front.main()
                    question_two = True

                else:
                    print("?????. You're supposed to only answer with a one or two\n")

        elif answer.lower() == "n" or answer.lower() == "no":
            """breaks out of the 2nd loop"""
            print("The Soviets are doomed\n"
                  "Good bye.")
            break

main()