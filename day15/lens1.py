with open("input.in", "r") as file:
    data = file.readlines()

answer = 0
all = []

for i, line in enumerate(data): 
    all = line.split(",")    

for i in all:
    ascii = 0
    for char in i:
        ascii += ord(char)
        ascii *= 17
        ascii %= 256
    answer += ascii
print(answer)