def kthSmallest(root, k):

    output = []

    def inorder(root):

        if not root:
            return

        inorder(root.left)
        output.append(root.val)
        inorder(root.right)
    inorder(root)
    return output[k-1]
