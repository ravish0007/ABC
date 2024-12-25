# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or  len(lists) == 0:
            return None
        
        
        while len(lists) > 1:
            mergedlists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                mergedlists.append(self.merge(list1, list2))
            lists = mergedlists
        return lists[0]
    
    def merge(self, l1, l2):

        node = ListNode(0)
        curr = node
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        return node.next
