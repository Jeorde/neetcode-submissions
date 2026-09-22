from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands+=1
                    grid[row][col] = "0"

                    queue = deque([(row,col)])
                    while queue:
                        r,c = queue.popleft()

                        for dr, dc in directions:
                            newRow = r+dr
                            newCol = c+dc

                            if 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol]=="1":
                            
                                queue.append((newRow,newCol))
                                grid[newRow][newCol] = "0"
            
        return islands
