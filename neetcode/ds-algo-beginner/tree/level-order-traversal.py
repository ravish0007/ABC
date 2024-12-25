class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []

        queue = deque()

        if root:
            queue.append(root)

        
        while len(queue) > 0:
            intermediate_output = []
            for i in range(len(queue)):
                node = queue.popleft()
                intermediate_output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(intermediate_output[:])
