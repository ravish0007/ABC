



def rightside(root):

    output = []

    queue = deque()
    queue.append(root)

    while queue:
        rightside = None
        for  i in range(len(queue)):
            node = queue.popleft()
            if node:
                rightside = node
                queue.append(node.left)
                queue.append(node.right)
        if rightside:
            output.append(rightside.val)
    return output

