# Add up all part numbers in the engine schematic (puzzle input)
# Any number adjacent to a symbol is a "part number" and included in sum
from collections import defaultdict
total = 0
numbers = "0123456789"
symbols = "!@#$%^&*()+=-/"
geardict = defaultdict(list)
answer = 0

with open("input.in", "r") as file:
    data = file.readlines()

for lineNum, line in enumerate(data):
    inNumber = False
    partialNumber = ""
    for i, number in enumerate(line):
        if number in numbers:
            if not inNumber:
                inNumber = True
                partialNumber += number
            else:
                partialNumber += number

        if number not in numbers or i == len(line)-1:
            if inNumber:
                #check top/left/right/bottom
                startIndex = i - len(partialNumber)
                endIndex = i
                symbolPresent = False
                #above
                for p in range(startIndex-1, endIndex+1):
                    try: 
                        if data[lineNum-1][p] in symbols:
                            symbolPresent = True
                            if data[lineNum-1][p] == "*":
                                geardict[(lineNum-1, p)].append(int(partialNumber))
                    except:
                        pass
                #below
                for p in range(startIndex-1, endIndex+1):
                    try: 
                        if data[lineNum+1][p] in symbols:
                            symbolPresent = True
                            if data[lineNum+1][p] == "*":
                                geardict[(lineNum+1, p)].append(int(partialNumber))
                    except:
                        pass
                #left
                try: 
                    if line[startIndex-1] in symbols:
                        symbolPresent = True
                        if line[startIndex-1] == "*":
                            geardict[(lineNum, startIndex-1)].append(int(partialNumber))
                except:
                    pass
                #right
                try: 
                    if line[endIndex] in symbols:
                        symbolPresent = True
                        if line[endIndex] == "*":
                            geardict[(lineNum, endIndex)].append(int(partialNumber))
                except:
                    pass
                if symbolPresent:
                    try:
                        answer += int(partialNumber)
                    except:
                        pass
                partialNumber = ""
                inNumber = False
answer = 0
for key, items in geardict.items():
    if len(items)==2:
        answer += items[0] * items[1]
print(answer)