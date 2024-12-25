

def construct_tree(inorder, preorder):
    
    if not inorder or not preorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = construct_tree(preorder[1:mid+1], inorder[:mid])
    root.right = construct_tree(preorder[mid+1:], inorder[mid+1:])
    return root
