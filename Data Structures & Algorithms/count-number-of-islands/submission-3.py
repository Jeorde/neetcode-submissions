class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row,col):

            if not (0<=row<rows and 0<=col<cols):
                return #Se index out of range da matriz, retorna
            if grid[row][col] != "1":
                return #Se for agua, retorna
            
            #Se chegou até aqui, está dentro da matriz E é terra
            grid[row][col] = "0" #Marca como visitado, ou agua nesse caso

            dfs(row+1, col) #Vizinho debaixo
            dfs(row-1,col) #Vizinho de cima
            dfs(row,col+1) #Vizinho da direita
            dfs(row,col-1) #Vizinho da esquerda
        
        for row in range(rows): #Pra cada linha
            for col in range(cols): #Pra cada coluna
                if grid[row][col] == "1": #Se encontrar uma ilha
                    islands+=1 #Aumenta counter
                    dfs(row,col) #Visita todos seus vizinhos para marca-los como visitados
        return islands