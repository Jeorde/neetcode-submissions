class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        islands = 0
        
        def neighbors(row, col):
            result = []
            direction = [
                (1,0), #Baixo
                (-1,0), #Cima
                (0,1), #Dir
                (0,-1) #Esq
            ]
            for dr, dc in direction:
                newRow = row+dr
                newCol = col+dc
                if(0 <= newRow < len(grid) and 0 <= newCol < len(grid[0])):
                    result.append((newRow,newCol))
            return result

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    islands+=1
                    visited.add((row,col))

                    queue = deque([(row,col)])
                    while queue:
                        cur = queue.popleft()
                        for newRow, newCol in neighbors(cur[0],cur[1]):
                            if grid[newRow][newCol] == "1" and (newRow,newCol) not in visited:
                                visited.add((newRow,newCol))
                                queue.append((newRow,newCol))
                 
        return islands
