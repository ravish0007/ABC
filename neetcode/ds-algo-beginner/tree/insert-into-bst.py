class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
