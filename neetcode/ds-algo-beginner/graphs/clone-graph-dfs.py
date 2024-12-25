class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        if not node:
            return None
            
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
             
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        dfs(node)
        return old_to_new[node] 
