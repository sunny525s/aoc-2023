from collections import defaultdict 

with open("input.in", "r") as file:
    data = file.readlines()

final = 0
cards = defaultdict(int)

for i, line in enumerate(data): 
    cards[i] += 1
    # print(line)

    card, numbers = line.split(":")
    winners, answers = numbers.strip().split("|")

    winners = winners.strip().split()
    answers = answers.strip().split()

    counter = 0
    for answer in answers: 
        if answer in winners:
            counter += 1
            winners.remove(answer)
    for j in range(counter):
        cards[i+j+1] += cards[i]
        # print(cards[j+1], cards[i])
    # print(cards)

# print(cards)
final = 0
for value in cards.values():
    final += value

print(final)