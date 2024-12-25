class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -=1 
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        left = self.left
        right = self.left.next

        left.next = node
        node.prev = left
        node.next = right
        right.prev = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        left = self.right.prev
        right = self.right

        left.next = node
        node.prev = left
        node.next = right
        right.prev = node


    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -=1 

        if cur and index == 0:
  
            node = Node(val)
            left = cur.prev
            right = cur

            left.next = node
            node.prev = left
            node.next = right
            right.prev = node


    def deleteAtIndex(self, index: int) -> None:

        cur = self.left.next
        while cur and  index > 0:
            cur = cur.next
            index -=1 
        if cur and cur != self.right and index == 0:
            left, right = cur.prev, cur.next
            left.next = right
            right.prev = left

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
