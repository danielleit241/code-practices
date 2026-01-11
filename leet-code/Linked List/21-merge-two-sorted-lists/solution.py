from typing import Optional
from ..ListNode import ListNode

class Solution: 
    def mergeTwoLists_Merge1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        res = ListNode(0)
        curr = res

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return res.next
    
    def mergeTwoLists_Merge2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        res = ListNode(0)
        curr = res

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return res.next
    
    def mergeTwoLists_Recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_Recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_Recursive(list1, list2.next)
            return list2