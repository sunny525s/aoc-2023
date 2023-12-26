# Add up all part numbers in the engine schematic (puzzle input)
# Any number adjacent to a symbol is a "part number" and included in sum
total = 0

numbers = "0123456789"
symbols = "!@#$%^&*()+=-/"

with open("input.in", "r") as file:
    data = file.readlines()

for lineNum, line in enumerate(data):
    num = False
    partialNum = ""
    for i, number in enumerate(line):
        if number in numbers:
            if not num:
                num = True
                partialNum += number
            else:
                partialNum += number

        if number not in numbers or i == len(line)-1:
            if num:
                startIndex = i - len(partialNum)
                endIndex = i
                symbolPresent = False
                #left
                print("checking left")
                try: 
                    print("checking", line[startIndex-1], lineNum)
                    if line[startIndex-1] in symbols:
                        symbolPresent = True
                except:
                    pass
                #right
                try: 
                    if line[endIndex] in symbols:
                        symbolPresent = True
                except:
                    pass
                #above
                for p in range(startIndex-1, endIndex+1):
                    try: 
                        if data[lineNum-1][p] in symbols:
                            symbolPresent = True
                    except:
                        pass
                #below
                for p in range(startIndex-1, endIndex+1):
                    try: 
                        print("checking", data[lineNum+1][p], lineNum, i)
                        if data[lineNum+1][p] in symbols:
                            symbolPresent = True
                    except:
                        pass
                if symbolPresent:
                    try:
                        total += int(partialNum)
                    except:
                        pass
                partialNum = ""
                num = False
    print(line)
print(total)