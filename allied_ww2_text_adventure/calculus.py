import math
def compute_pi():
    number = 0
    for i in range(0, 2):
        g = (math.fmod(i + math.pi, 2 * math.pi) - math.pi)
        number = (g - (1/3)*math.pow(g, 3) + (1/5)*math.pow(g, 5) + (1/7)*math.pow(g, 7) +
                  (1/9)*math.pow(g, 9) + (1/11)*math.pow(g,11))
        print(number)

def main():
    compute_pi()

main()