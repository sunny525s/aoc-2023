import sys

totals = 0
for line in sys.stdin:
    # print(line.split(":"))
    game, draws = line.split(":")
    id = int(game.split()[1])

    draws = draws.split(";")
    # print(draws)

    for draw in draws: 
        individuals = draw.strip().split(",")
        print(individuals)
        check = False
        for individual in individuals:
            red, blue, green = 0, 0, 0
            colors = individual.strip().split()
            if colors[1] == "green":
                green = int(colors[0])
            elif colors[1] == "red":
                red = int(colors[0])
            elif colors[1] == "blue":
                blue = int(colors[0])

            if red > 12 or green > 13 or blue > 14:
                check = True
                break
        if check:
            break
    if not check:
        totals += id
print(totals)