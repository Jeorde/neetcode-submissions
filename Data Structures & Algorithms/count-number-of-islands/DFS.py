class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols):
                return

            if grid[row][col] != "1":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands+=1
                    dfs(row,col)
        return islands
