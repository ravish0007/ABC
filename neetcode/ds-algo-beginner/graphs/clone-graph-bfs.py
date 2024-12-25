class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        old_to_new = {}
        if not node:
            return None

        q = collections.deque()
        q.append(node)

        copy = Node(node.val)
        old_to_new[node] = copy

        while q:
            u = q.popleft()
            ns = u.neighbors

            for n in ns:
                if n not in old_to_new:
                    nnode = Node(n.val)
                    old_to_new[n] = nnode
                    q.append(n)
                old_to_new[u].neighbors.append(old_to_new[n])

        return old_to_new[node] 
