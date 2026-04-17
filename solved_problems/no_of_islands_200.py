# First Solution: Using Recursive DFS

def numIslands(grid) -> int:
    if not grid:
        return 0
    
    visited = set()
    no_of_islands = 0
    rows, cols = len(grid), len(grid[0])
    directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

    def traverse(i, j):
        if (i, j) in visited:
            return 
        
        visited.add((i, j))
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols and grid[i][j] == '1':
                traverse(next_i, next_j)
    

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == '1':
                traverse(i, j)
                no_of_islands += 1
    
    return no_of_islands

# Second Solution: Using BFS (No Recursion) using Queue (for python deque or list).\
#                -> Since deque is faster in poping operation taking deque. List implementations can also be similar
from collections import deque

def numIslands(grid) -> int:
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
                    queue.append((next_i, next_j))
        
    
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == '1':
                traverse(i, j)
                no_of_islands += 1
    
    return no_of_islands

# Third Solution: Using DFS (Iterative) using Stack (using deque which can be used for stack and queues based on requirements)
def numIslands(grid) -> int:
    if not grid:
        return 0

    visited = set()
    no_of_islands = 0
    rows, cols = len(grid), len(grid[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(i, j):
        stack = deque()
        stack.append((i, j))

        while stack:
            curr_i, curr_j = stack.pop()

            if (curr_i, curr_j) in visited:
                continue
            
            visited.add((curr_i, curr_j))

            for direction in directions:
                next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == '1':
                    stack.append((next_i, next_j))
    

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == '1':
                dfs(i, j)
                no_of_islands += 1

    return no_of_islands
