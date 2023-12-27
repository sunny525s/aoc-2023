with open("input.in", "r") as file:
    data = file.readlines()

final = 0
for line in data: 
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
    # print(counter,  2**(max(0, counter-1)))
    if counter > 0:
        final += 2**(counter-1)
    # print(card, winners, answers)
print(final)