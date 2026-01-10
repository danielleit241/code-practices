from typing import Optional
from ..ListNode import ListNode

class Solution:
    def reverseList_Array(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        values = []
        curr = head
        while curr: 
            values.append(curr.val)
            curr = curr.next
        
        values.reverse()

        curr = head
        for val in values:
            curr.val = val
            curr = curr.next

        return head
    
    def reverseList_2Pointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev