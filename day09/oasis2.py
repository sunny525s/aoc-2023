with open("input.in", "r") as file:
    data = file.readlines()

answer = 0
for i, line in enumerate(data): 
    triangle = [[int(x) for x in line.split()]]
    while True: 
        newlist = []
        for j in range(len(triangle[len(triangle)-1])-1):
            newlist.append(triangle[len(triangle)-1][j+1]-triangle[len(triangle)-1][j])
        triangle.append(newlist)
        
        flag = True
        for item in triangle[-1]:
            if item != 0:
                flag = False
        if flag:
            break

    for j in range(len(triangle)-1, -1, -1):
        if j == len(triangle)-1:
            triangle[j].insert(0, 0)
        else:
            triangle[j].insert(0, triangle[j][0] - triangle[j+1][0])
    answer += triangle[0][0]
print(answer)