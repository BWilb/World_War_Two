def convert_binary(num):
    twos = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32,
            16, 8, 4, 2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125,
            0.00390625, 0.001953125]
    binary = []
    for i in range(len(twos)):
        if (num >= twos[i]):
            binary.append(1)
            num -= twos[i]
        elif (num <= twos[i]):
            binary.append(0)

    return binary

def main():
    response = False
    question = input("would you like to convert into binary?: ")
    if question == "yes":
        while not response:
            number = float(input("Hello user. Please insert a number: "))
            binary = convert_binary(number)
            print(f"{binary}")
            q2 = input("\nwould you like to convert another num into binary?: ")
            if q2 == "yes":
                continue
            elif q2 == "no":
                response = True
            else:
                print("I dont understand what you mean")

    elif question == "no":
        print("HAH")

main()