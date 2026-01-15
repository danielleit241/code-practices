from typing import Optional
from ..ListNode import ListNode

class Solution:
    # Time Complexity: O(max(m, n))
    # Space Complexity: O(max(m, n))
    def addTwoNumbers_Recursive(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addLists(n1: Optional[ListNode], n2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if not n1 and not n2 and carry == 0:
                return None

            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0

            total = val1 + val2 + carry
            new_carry = total // 10
            node = ListNode(total % 10)

            next1 = n1.next if n1 else None
            next2 = n2.next if n2 else None
            node.next = addLists(next1, next2, new_carry)

            return node
        
        return addLists(l1, l2, 0)
    
    # Time Complexity: O(max(m, n))
    # Space Complexity: O(1)
    def addTwoNumbers_Pointer(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next