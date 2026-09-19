class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        newGraph = {}

        def dfs(current):
            if current in newGraph:
                return newGraph[current]

            newGraph[current] = Node(current.val)

            for neighbor in current.neighbors:
                cloned_neighbor = dfs(neighbor)
                newGraph[current].neighbors.append(cloned_neighbor)
            return newGraph[current]

        return dfs(node)
