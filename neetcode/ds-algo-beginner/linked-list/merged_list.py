class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged_list = ListNode()
        merged_list_head = merged_list

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            val1 = curr1.val
            val2 = curr2.val

            if(val1 < val2):
                node = ListNode(val1)
                merged_list.next = node
                merged_list = node
                curr1 = curr1.next
            else:
                node = ListNode(val2)
                merged_list.next = node
                merged_list = node
                curr2 = curr2.next  

        if curr1:
            merged_list.next = curr1

        elif curr2:
            merged_list.next = curr2

        return merged_list_head.next    
