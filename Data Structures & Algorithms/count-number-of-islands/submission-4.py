class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [
            (1,0), #Baixo
            (-1,0), #Cima
            (0,1), #Direita
            (0,-1) #Esquerda
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1": #Se encontrar land
                    islands+=1 #Aumenta ilha
                    grid[row][col] == "0" #Seta como visitado/0
                    queue = deque([(row,col)]) #Adiciona a queue
                    while queue: #While queue is not empty
                        r, c = queue.popleft() #Pega o atual
                        for dR, dC in directions: #Aplica as direções com unpacking também
                            newRow = r+dR
                            newCol = c+dC
                            if(0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol] == "1"): #Verifica se está na matriz E é terra, se for, adiciona a queue para visitar seus vizinhos também, e marca como visitado
                                queue.append((newRow,newCol))
                                grid[newRow][newCol] = "0"
        return islands

