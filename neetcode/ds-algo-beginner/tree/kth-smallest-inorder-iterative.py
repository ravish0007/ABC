

def kthsmallest(root, k):

    curr = root
    stack = []
    n = 0


    while curr or stack:
        while curr:
            stack.append(curr.left)
            curr = curr.left
        curr = stack.pop()
        n += 1
        if (n == k):
            return curr.val
        curr = curr.right

