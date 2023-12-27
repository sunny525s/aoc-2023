import sys

total = 0

for line in sys.stdin:

    print(line.split(":"))
    game, draws = line.split(":")
    id = int(game.split()[1])

    draws = draws.split(";")
    print(draws)

    maxred, maxblue, maxgreen = 0, 0, 0

    for draw in draws: 
        individuals = draw.strip().split(",")
        print(individuals)
        check = False

        for individual in individuals:
            red, blue, green = 0, 0, 0
            colors = individual.strip().split()
            if colors[1] == "green":
                green = int(colors[0])
                maxgreen = max(maxgreen, green)
            elif colors[1] == "red":
                red = int(colors[0])
                maxred = max(maxred, red)
            elif colors[1] == "blue":
                blue = int(colors[0])
                maxblue = max(maxblue, blue)

    total += maxred * maxblue * maxgreen

print(total)