from collections import deque

def read_input(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def count_reachable_garden_plots(grid, max_steps):
    rows, cols = len(grid), len(grid[0])
    start_position = None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_position = (i, j)
                break

    queue = deque([(start_position, 0)])
    visited = set([start_position])

    while queue:
        (x, y), steps = queue.popleft()

        if steps == max_steps:
            continue

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            new_position = (nx, ny)

            if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.' and (new_position, steps+1) not in queue):
                if (steps==max_steps-1):
                    visited.add(new_position)
                queue.append((new_position, steps + 1))

    return len(visited)

def main():
    filename = 'input.in'
    grid = read_input(filename)
    max_steps = 64

    result = count_reachable_garden_plots(grid, max_steps)

    print(f"The Elf can reach {result} garden plots in exactly {max_steps} steps.")

if __name__ == "__main__":
    main()