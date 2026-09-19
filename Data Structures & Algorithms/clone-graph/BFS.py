class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        newGraph = {}
        queue = deque([node])
        visited = set([node])

        while queue:
            current_node = queue.popleft()

            if current_node not in newGraph:
                newGraph[current_node] = Node(current_node.val)

            for neighbor in current_node.neighbors:
                if neighbor not in newGraph:
                    newGraph[neighbor] = Node(neighbor.val)

                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

                newGraph[current_node].neighbors.append(newGraph[neighbor])

        return newGraph[node]
