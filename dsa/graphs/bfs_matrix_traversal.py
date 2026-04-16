# Leetcode 200: number of Islands

from collections import deque

def bfs(grid):
    if not grid:
        return 0
    
    visited = set()
    no_of_islands = 0
    rows, cols = len(grid), len(grid[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        queue = deque([(i, j)])

        while queue:
            curr_i, curr_j = queue.popleft()

            if (curr_i, curr_j) in visited:
                continue

            visited.add((curr_i, curr_j))

            for direction in directions:
                next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == '1':
                    traverse(next_i, next_j)

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == '1':
                traverse(i, j)
                no_of_islands += 1

    return no_of_islands

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

result = bfs(grid)
print(result)