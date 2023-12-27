with open("input.in", "r") as file:
    data = file.readlines()

answer = 1
beats, times, dists = [], [], []

for i, line in enumerate(data): 
    if i == 1:
        dists = [int(x) for x in line.split()[1:]]
    elif i == 0:
        times = [int(x) for x in line.split()[1:]]

for time, dist in zip(times, dists):
    beatcounter = 0
    for i in range(time + 1): 
        if i * (time - i) > dist:
            beatcounter += 1
    beats.append(beatcounter)

for beat in beats:
    answer *= beat

print(answer)